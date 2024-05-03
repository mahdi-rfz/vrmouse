import screen_tool
import keyboard
import pyautogui as pygui
import os 
import time 
from colorama import Fore

def clear_screen():  #clear screen for widows/linux/mac
    if os.name == "nt":
        os.system("cls")
    else :
        os.system("clear")
        
def typography():
    return"""██╗   ██╗██████╗ ███╗   ███╗ ██████╗ ██╗   ██╗███████╗███████╗
██║   ██║██╔══██╗████╗ ████║██╔═══██╗██║   ██║██╔════╝██╔════╝
██║   ██║██████╔╝██╔████╔██║██║   ██║██║   ██║███████╗█████╗  
╚██╗ ██╔╝██╔══██╗██║╚██╔╝██║██║   ██║██║   ██║╚════██║██╔══╝  
 ╚████╔╝ ██║  ██║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║███████╗
  ╚═══╝  ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝"""

        
def keys_input ():
    clear_screen()
    
    print(typography())
    
    print(Fore.LIGHTYELLOW_EX + f"""Note : if you want to use special key 
          like shift , enter , etc use numbers ::::""")
    time.sleep(0.5)
    print(f"""
          {Fore.CYAN}[k1] {Fore.WHITE}Alt
          {Fore.CYAN}[k2] {Fore.WHITE}Ctrl
          {Fore.CYAN}[k3] {Fore.WHITE}Esc
          {Fore.CYAN}[k4] {Fore.WHITE}Shift
          {Fore.CYAN}[k5] {Fore.WHITE}Delete""")
    click = input(Fore.WHITE + "Enter key or menu numbers for click key (press Enter for Enter KEY):").strip() or ("enter")
    print(Fore.CYAN + "================================================================")
    rightclick = input(Fore.WHITE + "Enter key or menu numbers for right click key (press Enter for Right shift KEY):").strip() or ("right shift")
    print(Fore.CYAN + "================================================================")
    upkey = input(Fore.WHITE + "Enter key or menu numbers for up key (press Enter for UP KEY):").strip() or ("up")
    print(Fore.CYAN + "================================================================")
    downkey = input(Fore.WHITE + "Enter key or menu numbers for down key (press Enter for DOWN KEY):").strip() or ("down")
    print(Fore.CYAN + "================================================================")
    rightkey = input(Fore.WHITE + "Enter key or menu numbers for right key (press Enter for RIGHT KEY):").strip() or ("right")
    print(Fore.CYAN + "================================================================")
    leftkey = input(Fore.WHITE + "Enter key or menu numbers for left key (press Enter for LEFT KEY):").strip() or ("left")
    print(Fore.CYAN + "================================================================")
    dpi = int(input(Fore.WHITE + "Enter DPI number (press Enter for '15'):").strip() or (15))
    
    #all condition for click
    click = "alt" if click == "k1" else click 
    click = "ctrl" if click == "k2" else click 
    click = "esc" if click == "k3" else click 
    click = "shift" if click == "k4" else click 
    click = "delete" if click == "k5" else click 
    
    #all condition for right click 
    rightclick = "alt" if rightclick == "k1" else rightclick 
    rightclick = "ctrl" if rightclick == "k2" else rightclick 
    rightclick = "esc" if rightclick == "k3" else rightclick 
    rightclick = "shift" if rightclick == "k4" else rightclick 
    rightclick = "delete" if rightclick == "k5" else rightclick    
    
    # all condition for upkey
    rightclick = "alt" if rightclick == "k1" else rightclick 
    rightclick = "ctrl" if rightclick == "k2" else rightclick 
    rightclick = "esc" if rightclick == "k3" else rightclick 
    rightclick = "shift" if rightclick == "k4" else rightclick 
    rightclick = "delete" if rightclick == "k5" else rightclick 

    #all condition for downkey
    downkey = "alt" if downkey == "k1" else downkey 
    downkey = "ctrl" if downkey == "k2" else downkey 
    downkey = "esc" if downkey == "k3" else downkey 
    downkey = "shift" if downkey == "k4" else downkey 
    downkey = "delete" if downkey == "k5" else downkey 

    #all condition for rightkey
    rightkey = "alt" if rightkey == "k1" else rightkey 
    rightkey = "ctrl" if rightkey == "k2" else rightkey 
    rightkey = "esc" if rightkey == "k3" else rightkey 
    rightkey = "shift" if rightkey == "k4" else rightkey 
    rightkey = "delete" if rightkey == "k5" else rightkey 
    
    #all condition for leftkey
    leftkey = "alt" if leftkey == "k1" else leftkey 
    leftkey = "ctrl" if leftkey == "k2" else leftkey 
    leftkey = "esc" if leftkey == "k3" else leftkey 
    leftkey = "shift" if leftkey == "k4" else leftkey 
    leftkey = "delete" if leftkey == "k5" else leftkey 

    return [click , rightclick , upkey , downkey , rightkey , leftkey , dpi]


def main ():
    #click , rightclick , upkey , downkey , rightkey , leftkey , dpi
    keys_data = keys_input()
    clear_screen()
    
    print(typography())
    print(f"Screen size : {screen_tool.Screen_gin.screen_size()}")
    print("________________________________________________")
    print("Selected keys :")
    print(f"Click : {keys_data[0]}      ,Right Click : {keys_data[1]}")
    print(f"Up : {keys_data[2]}      ,Down : {keys_data[3]}")
    print(f"Right : {keys_data[4]}      ,Left : {keys_data[5]}")
    print(f"DPI number : {keys_data[6]}")
    print("================================================================")
    
    center = screen_tool.Screen_gin.center_finder()
    i = center[0]
    j = center[1]
    
    dpi = keys_data[6]
    pygui.moveTo (i , j)
    while True:
        received_key = keyboard.read_key()
        
        if received_key == keys_data[0] : #keys_data[0] for click 
            pygui.click()
        elif received_key == keys_data[1] :
            pygui.rightClick()
            
        elif received_key == keys_data[2]:
            j = j - dpi
            
        elif received_key == keys_data[3]:
            j = j + dpi
            
        elif received_key == keys_data[4]:
            i = i + dpi
            
        elif received_key == keys_data[5]:
            i = i - dpi            
            
        pygui.moveTo(i , j) 
        
main()