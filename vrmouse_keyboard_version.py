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
        
    if key_list[1] == "enter":
        key_list[1] = "right shift"
    if key_list[2] == "enter":
        key_list[2] = "up"
    if key_list[3] == "enter":
        key_list[3] = "down"
    if key_list[4] == "enter":
        key_list[4] = "right"
    if key_list[5] == "enter":
        key_list[5] = "left"
        
    return [key_list[0] , key_list[1] , key_list[2] , key_list[3] , key_list[4] , key_list[5] , dpi]



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
        if key == pykeyboard.Key.up:
            j = j - dpi
        elif key == pykeyboard.Key.down:
            j = j + dpi
        elif key == pykeyboard.Key.right:
            
            i = i + dpi
        elif key == pykeyboard.Key.left:
            i = i - dpi 
        pygui.moveTo(i , j) 
        if key ==  x:
            pygui.click()
        elif key == pykeyboard.Key.name("shift_r"):
            pygui.rightClick()
    except AttributeError:
        pass
    

def on_release(key):
    if key == pykeyboard.Key.esc:
        # Stop listener
        return False


keyboard.block_key('up')
keyboard.block_key('down')
keyboard.block_key('right')
keyboard.block_key('left')

with pykeyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    