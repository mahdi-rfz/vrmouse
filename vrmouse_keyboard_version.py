import screen_tool
import keyboard
import pyautogui as pygui
import os 
import time 
from colorama import Fore

#for later :
# 1 - change dpi with keys on keyboard 
# 2 - add additional buttons
# 3 - add data base

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
    ######################################add [] in menu for q
    arg_key = 0
    key_list = []
    key_name = ["Click" , "RightClick" , "Up" , "Down" , "Right" , "Left"]
    def_key = ["Enter" , "Right Shift" , "UP" , "Down" , "Right" , "Left "]
    while True:
        print(Fore.WHITE + f"Press the key you want for  {key_name[arg_key]} (press Enter for {def_key[arg_key]} key) : ")
        key_input = keyboard.read_key() #I repeated this twice because of a problem that the keyboard library 
        key_input = keyboard.read_key() #and counted the pressure twice each time.
        print(Fore.CYAN + "================================================================")
        key_list.append(key_input)
        arg_key = arg_key + 1
        if arg_key == 6:
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


def main ():
    #click , rightclick , upkey , downkey , rightkey , leftkey , dpi
    keys_data = keys_input()
    clear_screen()
    
    print(typography())
    print(f"{Fore.LIGHTBLACK_EX}Screen size : {Fore.LIGHTGREEN_EX + str(screen_tool.Screen_gin.screen_size())}")
    print(Fore.WHITE +"________________________________________________")
    print(Fore.LIGHTBLACK_EX + "Selected keys :")
    print(f"{Fore.LIGHTBLACK_EX}Click : {Fore.LIGHTGREEN_EX + keys_data[0]}      ,{Fore.LIGHTBLACK_EX}Right Click : {Fore.LIGHTGREEN_EX + keys_data[1]}")
    print(f"{Fore.LIGHTBLACK_EX}Up : {Fore.LIGHTGREEN_EX + keys_data[2]}      ,{Fore.LIGHTBLACK_EX}Down : {Fore.LIGHTGREEN_EX + keys_data[3]}")
    print(f"{Fore.LIGHTBLACK_EX}Right : {Fore.LIGHTGREEN_EX + keys_data[4]}      ,{Fore.LIGHTBLACK_EX}Left : {Fore.LIGHTGREEN_EX + keys_data[5]}")
    print(f"{Fore.LIGHTBLACK_EX}DPI number : {Fore.LIGHTGREEN_EX + str(keys_data[6])}")
    print(Fore.WHITE + "================================================================")
    
    center = screen_tool.Screen_gin.center_finder()
    i = center[0]
    j = center[1]
    
    dpi = keys_data[6]
    pygui.moveTo (i , j)
    
     #click , rightclick , upkey , downkey , rightkey , leftkey , dpi
    while True:
        received_key = keyboard.read_key()
        
        if received_key == keys_data[0] : #keys_data[0] for click 
            pygui.click()
        elif received_key == keys_data[1] :
            pygui.rightClick()
            
        elif received_key == keys_data[2]: #up
            j = j - dpi
            
        elif received_key == keys_data[3]:
            j = j + dpi
            
        elif received_key == keys_data[4]:#right
            i = i + dpi
            
        elif received_key == keys_data[5]:
            i = i - dpi            
            
        pygui.moveTo(i , j) 

        
main()