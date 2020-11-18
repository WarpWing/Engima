from consolemenu import *
from consolemenu.items import *
from mpsfunc import * 
import sys
import getpass
import time
import pretty_errors
import os

# File Wide Variables
app = 'MultipassSimplified'
username = getpass.getuser()
m = f'/home/{username}/snap/multipass'  # Linux
w = f"c:/Program Files/multipass"       # Windows
isFile = os.path.isdir(m) 

#Multipass Install Check
def multipassCheck():
    if isFile: 
        pass
    else: 
        print(f"Please install Multipass before launching {app} ") 
        exit()


# GUI Logic 
def mainConsole():
    # GUI Logic 
    menu = ConsoleMenu("MultipassSimplified", "A Python TUI Interface for the Multipass VM System by WarpWing")
    # Command Logic 
    command_item1 = FunctionItem("Create New MP Instance", warpwing)
    # Menu Append Array
    menu.append_item(command_item1)
    # Menu Show Function 
    menu.show()     
# Invoking Multipass Check
multipassCheck() 
# Invoke Console
mainConsole()
