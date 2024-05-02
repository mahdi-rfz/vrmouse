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
        
        
def main ():
    clear_screen()
    
    print(Fore.WHITE + """██╗   ██╗██████╗ ███╗   ███╗ ██████╗ ██╗   ██╗███████╗███████╗
██║   ██║██╔══██╗████╗ ████║██╔═══██╗██║   ██║██╔════╝██╔════╝
██║   ██║██████╔╝██╔████╔██║██║   ██║██║   ██║███████╗█████╗  
╚██╗ ██╔╝██╔══██╗██║╚██╔╝██║██║   ██║██║   ██║╚════██║██╔══╝  
 ╚████╔╝ ██║  ██║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝███████║███████╗
  ╚═══╝  ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
""")
    
    print(Fore.LIGHTYELLOW_EX + f"""Note : if you want to use special key 
          like shift , enter , etc use numbers ::::""")
    time.sleep(0.5)
    print(f"""
          {Fore.CYAN}[k1] {Fore.WHITE}Alt
          {Fore.CYAN}[k2] {Fore.WHITE}Ctrl
          {Fore.CYAN}[k3] {Fore.WHITE}Esc
          {Fore.CYAN}[k4] {Fore.WHITE}Shift
          {Fore.CYAN}[k5] {Fore.WHITE}Delete""")
    
    upkey = input("Enter key or menu numbers for up key (press Enter for UP KEY):").strip() or ("up")
    print("================================================================")
    downkey = input("Enter key or menu numbers for down key (press Enter for DOWN KEY):").strip() or ("down")
    print("================================================================")
    rightkey = input("Enter key or menu numbers for right key (press Enter for RIGHT KEY):").strip() or ("right")
    print("================================================================")
    leftkey = input("Enter key or menu numbers for left key (press Enter for LEFT KEY):").strip() or ("left")
    
    # all condition for upkey
    upkey = "alt" if upkey == "k1" else upkey 
    upkey = "ctrl" if upkey == "k2" else upkey 
    upkey = "esc" if upkey == "k3" else upkey 
    upkey = "shift" if upkey == "k4" else upkey 
    upkey = "delete" if upkey == "k5" else upkey 

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



main()

