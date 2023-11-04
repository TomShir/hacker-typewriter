import time 
import sys 
from colorama import Fore 
from readchar import readkey,key 
enter_button=key.ENTER 
font_color=Fore.GREEN
open_txt_file=open('hack.txt','r')
text=open_txt_file.readlines()
hack_mode=input('automatic or typed:')
def hack_script(mode):
    if mode=='automatic' or mode=='typed':
     for txt in text:
        sys.stdout.flush()
        time.sleep(0.0001)
        print(f'{font_color}{txt}',flush=True)
        if mode=='typed':
            if readkey()==enter_button:
                break 
        else:
            pass
def execute_script(mode_1,mode_2,input_mode):
    if input_mode==mode_1:
        hack_script(mode=mode_1)
    elif input_mode==mode_2:
        if readkey():
            hack_script(mode=mode_2)
        elif readkey==enter_button:
            sys.exit('')
            
execute_script(mode_1='automatic',mode_2='typed',input_mode=hack_mode)