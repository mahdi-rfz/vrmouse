import screen_tool
import keyboard
import pyautogui as pygui
import os 
from pynput import keyboard as pykeyboard
import time 
from colorama import Fore

'''NEXT :
1 - add live dpi controller
2 - costume exit buttone 
'''



'''
Explanation of variables :

'''

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

        
def input_keys_function ():
    clear_screen()
    
    print(typography())
    
    print(Fore.LIGHTYELLOW_EX + f"""::::Choose from CTRL, Alt and Shift keys, our suggestion is the default::::
          """)
    
    input_counter = 0
    keys_received_list = []
    key_function = ["Click" , "RightClick" , "Exit"]
    default_key_name = ["Enter" , "Right Shift" , "ESC"]
    key_sign = ["C" , "RC" , "E"]
    while True:
        print(Fore.WHITE + f"{Fore.GREEN}[{key_sign[input_counter]}]{Fore.WHITE} Press the key you want for  {key_function[input_counter]} (press Enter for {default_key_name[input_counter]} key) : ")
        input_keys = keyboard.read_key()                  #I repeated this twice because of a problem that the keyboard library 
        input_keys = keyboard.read_key()                  #and counted the pressure twice each time.
        print(Fore.LIGHTBLACK_EX + "================================================================")
        keys_received_list.append(input_keys)
        input_counter = input_counter + 1
        if input_counter == 3:
            break

    input()
    print(Fore.LIGHTBLACK_EX + ":::::::::( Press Enter ):::::::::")
    input()
    input()
    
    while True :
        dpi = ("Hello Reader")
        try :
            dpi = int(input(f"{Fore.GREEN}[DPI]{Fore.WHITE} Enter the number you want for DPA (Between {Fore.LIGHTYELLOW_EX}5-50{Fore.WHITE})(press Enter for '20') :").strip() or (20))
        except ValueError :
            pass
            print(Fore.RED + "::::::::::::::::( Use number to give input ):::::::::::::::")
        
        s1 , s2 = False , False
        if type(dpi) == int:
            s1 = True
            if dpi < 5 or dpi > 50 :
                print(Fore.RED + "::::::::::::::::( The number you entered was out of range ):::::::::::::::")
            else :
                s2 = True
            if s1 == True and s2 == True :
                break
        
            
        
    
    global block_keys_list
    #                   up  ,  down  ,  right  ,  left
    block_keys_list = ["up" , "down" , "right" , "left"]


    #cshow = click show           rcshow = right click show         eshow = exit show 
    global cshow , rcshow , eshow
    
    #all conditions for click     
    try :
        if keys_received_list[0] == "right ctrl" :
            keys_received_list[0] = pykeyboard.Key.ctrl_r
            cshow = ("RIGHT CTRL")
        if keys_received_list[0] == "ctrl" :
            keys_received_list[0] = pykeyboard.Key.ctrl_l
            cshow = ("CTRL")
        if keys_received_list[0] == "right alt" :
            keys_received_list[0] = pykeyboard.Key.alt_r
            cshow = ("RIGHT ALT")
        if keys_received_list[0] == "alt" :
            keys_received_list[0] = pykeyboard.Key.alt_l
            cshow = ("ALT")
        if keys_received_list[0] == "enter" :
            keys_received_list[0] = pykeyboard.Key.enter
            cshow = ("ENTER")
        e = cshow
    except NameError:
        keys_received_list[0] = pykeyboard.Key.enter
        cshow = ("ENTER")
        


    #all conditions for right click      
    try :                                          
        if keys_received_list[1] == "right ctrl" :
            keys_received_list[1] = pykeyboard.Key.ctrl_r
            rcshow = ("RIGHT CTRL")
        if keys_received_list[1] == "ctrl" :
            keys_received_list[1] = pykeyboard.Key.ctrl_l
            rcshow = ("CTRL")
        if keys_received_list[1] == "right alt" :
            keys_received_list[1] = pykeyboard.Key.alt_r
            rcshow = ("RIGHT ALT")
        if keys_received_list[1] == "alt" :
            keys_received_list[1] = pykeyboard.Key.alt_l
            rcshow = ("ALT")
        if keys_received_list[1] == "enter" :
            keys_received_list[1] = pykeyboard.Key.shift_r
            rcshow = ("RIGHT SHIFT")
        e = rcshow
    except NameError :
            keys_received_list[1] = pykeyboard.Key.ctrl_r
            rcshow = ("RIGHT CTRL")
    
    
    
      #all conditions for exit     
    try :                                          
        if keys_received_list[2] == "right ctrl" :
            keys_received_list[2] = pykeyboard.Key.ctrl_r
            eshow = ("RIGHT CTRL")
        if keys_received_list[2] == "ctrl" :
            keys_received_list[2] = pykeyboard.Key.ctrl_l
            eshow = ("CTRL")
        if keys_received_list[2] == "right alt" :
            keys_received_list[2] = pykeyboard.Key.alt_r
            eshow = ("RIGHT ALT")
        if keys_received_list[2] == "alt" :
            keys_received_list[2] = pykeyboard.Key.alt_l
            eshow = ("ALT")
        if keys_received_list[2] == "enter" :
            keys_received_list[2] = pykeyboard.Key.esc
            eshow = ("ESC")
        e = eshow
    except NameError :
            keys_received_list[2] = pykeyboard.Key.esc
            eshow = ("ESC")
    
    
    return [keys_received_list[0] , keys_received_list[1] ,keys_received_list[2], pykeyboard.Key.up , pykeyboard.Key.down , pykeyboard.Key.right , pykeyboard.Key.left , dpi]


#----------------------------------------------------main-----------------------------------------------------
#click , rightclick , exit , upkey , downkey , rightkey , leftkey , dpi


input_keys_ftf = input_keys_function()  #input keys ftf = input keys from the function

clear_screen()

print(typography())
print(f"{Fore.LIGHTBLACK_EX}Screen size : {Fore.LIGHTGREEN_EX + str(screen_tool.Screen_gin.screen_size())}")
print(Fore.LIGHTBLACK_EX + "Exit : " , Fore.LIGHTGREEN_EX + eshow)
print(Fore.WHITE +"________________________________________________")
print(Fore.LIGHTBLACK_EX + "Selected keys :")
print(f"{Fore.LIGHTBLACK_EX}Click : {Fore.LIGHTGREEN_EX + cshow}      {Fore.LIGHTBLACK_EX}Right Click : {Fore.LIGHTGREEN_EX + rcshow}")
print(f"{Fore.LIGHTBLACK_EX}Up : {Fore.LIGHTGREEN_EX }UP Key      {Fore.LIGHTBLACK_EX}Down : {Fore.LIGHTGREEN_EX }DOWN Key")
print(f"{Fore.LIGHTBLACK_EX}Right : {Fore.LIGHTGREEN_EX} RIGHT Key      {Fore.LIGHTBLACK_EX}Left : {Fore.LIGHTGREEN_EX}LEFT Key")
print(f"{Fore.LIGHTBLACK_EX}DPI number : {Fore.LIGHTGREEN_EX + str(input_keys_ftf[7])}")
print(Fore.WHITE + "================================================================")
print(Fore.CYAN + "             Coding by mahdi-rfz")
print(Fore.LIGHTCYAN_EX + "   Contact us : https://github.com/mahdi-rfz")
print(Fore.WHITE + "================================================================")
Fore.WHITE

center = screen_tool.Screen_gin.center_finder()
i =  center[0]
j =  center[1]
pygui.moveTo(i , j) 
#When the program starts, it moves the pointer 
# to the center of the screen for easy finding

'''Description
Here we have simulated the screen into
a two dimensional Cartesian with the 
pyautogui library , and i and j represent X and Y.
'''

dpi = input_keys_ftf[7]

def on_press(key):

    global i , j
    try:
        if key == input_keys_ftf[3]:
            j = j - dpi
        elif key == input_keys_ftf[4]:
            j = j + dpi
        elif key == input_keys_ftf[5]:
            i = i + dpi
        elif key == input_keys_ftf[6]:
            i = i - dpi 
        pygui.moveTo(i , j) 
        if key ==  input_keys_ftf[0]:
            pygui.click()
        elif key == input_keys_ftf[1]:
            pygui.rightClick()
            
    except AttributeError:
        pass
    

def on_release(key):
    if key == input_keys_ftf[2]:
        # Stop listener
        return False

#-----------------------------block selected key-----------------------------
keyboard.block_key(block_keys_list[0])
keyboard.block_key(block_keys_list[1])
keyboard.block_key(block_keys_list[2])
keyboard.block_key(block_keys_list[3])
#----------------------------------------------------------------------------


with pykeyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
