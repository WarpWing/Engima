import colorama
import os
import subprocess
import time
from colorama import Fore, Style
from consolemenu import *
from consolemenu.items import *

print(Fore.RED) #Declares default color. Will add multiple colors soon!

# GUI Logic 
def mainConsole():
    # GUI Logic 
    menu = ConsoleMenu("MultipassSimplified", "A Python TUI Interface for the Multipass VM System by WarpWing")
    # Command Logic 
    launchMP = FunctionItem("Create New MP Instance", launchMPI)
    shellMP = FunctionItem("Shell into MP Instance",shellMPI)
    # Menu Append Array
    menu.append_item(launchMP)
    menu.append_item(shellMP)
    # Menu Show Function 
    menu.show()     
# Launch MP Logic 
def launchMPI():
    print("What would like to name this MP Instance?")
    mpname = input("Name: ")
    print("How many CPUs would you like to allocate?")
    print("The minimum CPUs is 1 and the default CPU allocation is 1 if left blank")
    mpcpu = input("CPUs: ")
    print("How much Memory would you like to allocate?")
    print("Please use the suffixes of K,M or G in declaring memory.") 
    print("The minimum Memory is 128M and the default is 1G if left blank")
    mpmem = input("Memory: ")
    print("How much disk space would you like to allocate?")
    print("Please use the suffixes of K,M or G in declaring disk space.")
    print("The minimum storage is 512M and the default is 5G")
    mpdisk = input("Space: ")
    print(f"To finalize the creation of this MP Instance,please verify the following settings:")
    print(f"Name: {mpname}")
    print(f"CPUs: {mpcpu}")
    print(f"Memory: {mpmem}")
    print(f"Disk Space: {mpdisk}")
    mpfinal = input("Is this correct? y/n?: ")
    if mpfinal == "y":
        print("Creating MP Instance with the following settings")
        time.sleep(2)
        os.system(f"multipass launch -n {mpname} -c {mpcpu} -m {mpmem} -d {mpdisk}")
        print(f"Instance {mpname} created!")
        time.sleep(3)
    else: 
        print("Going back to the main menu!") # I'll work on a fix later that allows you to either resubmit settings or go back to the main menu.
        time.sleep(5)
# Shell MP Logic 

def shellMPI():
    print("---------------------------------------------------------------------------")
    x = subprocess.Popen("multipass list", shell=True, stdout=subprocess.PIPE)
    subprocess_return = x.stdout.read()
    print(subprocess_return.decode("ascii"))
    print("---------------------------------------------------------------------------")
    x = input(f"Please type the name of the instance you would like to shell into: ")
    os.system(f"multipass shell {x}")
    print(Fore.RED)
# Invoking Console
mainConsole()



