import pyautogui as pygui
import os   

class Screen_gin :
    def __init__(self):
            pass
        
    
    def center_finder():
        centeral = tuple(pygui.size())
        wcenter = centeral[0]
        hcenter = centeral[1]
        
        return [wcenter//2 , hcenter//2]
    #Dividing by two is for find center of the screen
    
    
    def screen_size():  #output screen size to list
        size = tuple(pygui.size())
        return [size[0] , size[1]]
    
    
    def try_range( width_try , height_try ): #try screen range like 0 <= x <= 1080
        size = tuple(pygui.size())
        if width_try <= size[0] and height_try <= size[1] :
            return True
        else :
            return False