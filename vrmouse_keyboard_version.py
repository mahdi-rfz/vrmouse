import screen_tool
import keyboard
import pyautogui as pygui
import os 
from pynput import keyboard as pykeyboard
import time 
from colorama import Fore



def clear_screen():  #clear screen for widows/linux/mac/maybe my os :)
    if os.name == "nt":
        os.system("cls")
    else :
        os.system("clear")
        
def typography(): #typography for script
    return Fore.WHITE + """██╗   ██╗██████╗ ███╗   ███╗ ██████╗ ██╗   ██╗███████╗███████╗
██║   ██║██╔══██╗████╗ ████║██╔═══██╗██║   ██║██╔════╝██╔════╝
██║   ██║██████╔╝██╔████╔██║██║   ██║██║   ██║███████╗█████╗  
╚██╗ ██╔╝██╔══██╗██║╚██╔╝██║██║   ██║██║   ██║╚════██║██╔══╝  
 ╚████╔╝ ██║  ██║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║███████╗
  ╚═══╝  ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝"""

        
def keys_input ():
    clear_screen()
    
    print(typography())
    
    print(Fore.LIGHTYELLOW_EX + f"""::::When receiving the keys, just press the key you want ::::
          """)
    
    key_arg = 0
    key_list = []
    key_name = ["Click" , "RightClick"]
    key_def = ["Enter" , "Right Shift"]
    key_sign = ["C" , "RC"]
    while True:
        print(Fore.WHITE + f"[{key_sign[key_arg]}] Press the key you want for  {key_name[key_arg]} (press Enter for {key_def[key_arg]} key) : ")
        key_input = keyboard.read_key() #I repeated this twice because of a problem that the keyboard library 
        key_input = keyboard.read_key() #and counted the pressure twice each time.
        print(Fore.CYAN + "================================================================")
        key_list.append(key_input)
        key_arg = key_arg + 1
        if key_arg == 2:
            break

    input()
    input()
    dpi = int(input(Fore.WHITE + "Enter the number you want for DPA (press Enter for '20') :").strip() or (20))
    
    global block_keys
    #         up , down , right , left
    block_keys = ["up" , "down" , "right" , "left"]  #have bug <---------------------------------
    #all conditions for block keys                                                  else for default
    key_data = ["up" , "down" , "right" , "left" , "w" , "w" , "8" , "2" , "s" , "S" , "6" , "d" , "D" , "4" , "a" , "A"]
    if block_keys[0] == "enter" :
        block_keys[0] = "up"
    if block_keys[1] == "enter" :
        block_keys[1] = "down"
    if block_keys[2] == "enter" :
        block_keys[2] = "right"
    if block_keys[3] == "enter" :
        block_keys[3] = "left"
    if block_keys[0] and block_keys[1] and block_keys[2] and block_keys[3] not in key_data :
        raise "out of range"
    
    #all conditions for click        
    ckey_data = ["right ctrl" , "ctrl" , "right alt" , "alt" , "enter"]
    if key_list[0] == "right ctrl" :
        key_list[0] = pykeyboard.Key.ctrl_r
    if key_list[0] == "ctrl" :
        key_list[0] = pykeyboard.Key.ctrl_l
    if key_list[0] == "right alt" :
        key_list[0] = pykeyboard.Key.alt_r
    if key_list[0] == "alt" :
        key_list[0] = pykeyboard.Key.alt_l
    if key_list[0] == "enter" :
        key_list[0] = pykeyboard.Key.enter


    #all conditions for right click                                                
    if key_list[1] == "right ctrl" :
        key_list[1] = pykeyboard.Key.ctrl_r
    if key_list[1] == "ctrl" :
        key_list[1] = pykeyboard.Key.ctrl_l
    if key_list[1] == "right alt" :
        key_list[1] = pykeyboard.Key.alt_r
    if key_list[1] == "alt" :
        key_list[1] = pykeyboard.Key.alt_l
    if key_list[1] == "enter" :
        key_list[1] = pykeyboard.Key.shift_r
    
    return [key_list[0] , key_list[1] , pykeyboard.Key.up , pykeyboard.Key.down , pykeyboard.Key.right , pykeyboard.Key.left , dpi]


#----------------------------------------------------main-----------------------------------------------------
#click , rightclick , upkey , downkey , rightkey , leftkey , dpi
keys_data = keys_input()
clear_screen()


center = screen_tool.Screen_gin.center_finder()
i =  center[0]
j =  center[1]

pygui.moveTo(i , j)
dpi = keys_data[6]

def on_press(key):

    global i , j
    try:
        if key == keys_data[2]:
            j = j - dpi
        elif key == keys_data[3]:
            j = j + dpi
        elif key == keys_data[4]:
            i = i + dpi
        elif key == keys_data[5]:
            i = i - dpi 
        pygui.moveTo(i , j) 
        if key ==  keys_data[0]:
            pygui.click()
        elif key == keys_data[1]:
            pygui.rightClick()
            
    except AttributeError:
        pass
    

def on_release(key):
    if key == pykeyboard.Key.esc:
        # Stop listener
        return False


keyboard.block_key(block_keys[0])
keyboard.block_key(block_keys[1])
keyboard.block_key(block_keys[2])
keyboard.block_key(block_keys[3])


with pykeyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
