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
    key_name = ["Click" , "RightClick" , "Up" , "Down" , "Right" , "Left"]
    key_def = ["Enter" , "Right Shift" , "UP" , "Down" , "Right" , "Left "]
    key_sign = ["C" , "RC" , "U" , "D" , "R" , "L"]
    while True:
        print(Fore.WHITE + f"[{key_sign[key_arg]}] Press the key you want for  {key_name[key_arg]} (press Enter for {key_def[key_arg]} key) : ")
        key_input = keyboard.read_key() #I repeated this twice because of a problem that the keyboard library 
        key_input = keyboard.read_key() #and counted the pressure twice each time.
        print(Fore.CYAN + "================================================================")
        key_list.append(key_input)
        key_arg = key_arg + 1
        if key_arg == 6:
            break
    dpi = int(input(Fore.WHITE + "Enter the number you want for DPA (press Enter for '20') :").strip() or (20))
    
    global block_keys
    #         up , down , right , left
    block_keys = [key_list[2] , key_list[3], key_list[4] , key_list[5]]  #have bug <---------------------------------
    #all conditions for click                                                     else for default
    key_list[0] = pykeyboard.Key.enter if key_list[0] == "enter" else key_list[0] == pykeyboard.Key.enter
    key_list[0] = pykeyboard.Key.enter if key_list[0] == "enter" else key_list[0] 
    key_list[0] = pykeyboard.Key.enter if key_list[0] == "enter" else key_list[0] 
    key_list[0] = pykeyboard.Key.enter if key_list[0] == "enter" else key_list[0] 
    key_list[0] = pykeyboard.Key.enter if key_list[0] == "enter" else key_list[0] 
    
    #all conditions for right click                                                
    key_list[1] = pykeyboard.Key.shift_r if key_list[1] == "enter" else key_list[1] == pykeyboard.Key.shift_r
    key_list[1] = pykeyboard.Key.enter if key_list[1] == "enter" else key_list[1] 
    key_list[1] = pykeyboard.Key.enter if key_list[1] == "enter" else key_list[1] 
    key_list[1] = pykeyboard.Key.enter if key_list[1] == "enter" else key_list[1] 
    key_list[1] = pykeyboard.Key.enter if key_list[1] == "enter" else key_list[1] 

    #all conditions for up
    key_list[2] = pykeyboard.Key.up if key_list[2] == "enter" else key_list[2] == pykeyboard.Key.up
    key_list[2] = pykeyboard.Key.enter if key_list[2] == "enter" else key_list[2] 
    key_list[2] = pykeyboard.Key.enter if key_list[2] == "enter" else key_list[2] 
    key_list[2] = pykeyboard.Key.enter if key_list[2] == "enter" else key_list[2] 
    key_list[2] = pykeyboard.Key.enter if key_list[2] == "enter" else key_list[2] 
        
    #all conditions for down
    key_list[3] = pykeyboard.Key.down if key_list[3] == "enter" else key_list[3] == pykeyboard.Key.down
    key_list[3] = pykeyboard.Key.enter if key_list[3] == "enter" else key_list[3] 
    key_list[3] = pykeyboard.Key.enter if key_list[3] == "enter" else key_list[3] 
    key_list[3] = pykeyboard.Key.enter if key_list[3] == "enter" else key_list[3] 
    key_list[3] = pykeyboard.Key.enter if key_list[3] == "enter" else key_list[3] 
        
    #all conditions for right
    key_list[4] = pykeyboard.Key.right if key_list[4] == "enter" else key_list[4] == pykeyboard.Key.right
    key_list[4] = pykeyboard.Key.enter if key_list[4] == "enter" else key_list[4] 
    key_list[4] = pykeyboard.Key.enter if key_list[4] == "enter" else key_list[4] 
    key_list[4] = pykeyboard.Key.enter if key_list[4] == "enter" else key_list[4] 
    key_list[4] = pykeyboard.Key.enter if key_list[4] == "enter" else key_list[4] 
    
    #all conditions for left
    key_list[5] = pykeyboard.Key.left  if key_list[5] == "enter" else key_list[5] == pykeyboard.Key.left
    key_list[5] = pykeyboard.Key.enter if key_list[5] == "enter" else key_list[5] 
    key_list[5] = pykeyboard.Key.enter if key_list[5] == "enter" else key_list[5] 
    key_list[5] = pykeyboard.Key.enter if key_list[5] == "enter" else key_list[5] 
    key_list[5] = pykeyboard.Key.enter if key_list[5] == "enter" else key_list[5] 
    
    
    return [key_list[0] , key_list[1] , key_list[2] , key_list[3] , key_list[4] , key_list[5] , dpi]


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
print(block_keys[2])

with pykeyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    