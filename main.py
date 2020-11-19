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
    stopMP = FunctionItem("Stop MP Instance",stopMPI)
    deleteMP = FunctionItem("Delete MP Instance",deleteMPI)
    purgeMP = FunctionItem("Purge deleted MP Instances",purgeMPI)
    # Menu Append Array
    menu.append_item(launchMP)
    menu.append_item(shellMP)
    menu.append_item(stopMP)
    menu.append_item(deleteMP)
    menu.append_item(purgeMP)
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
        os.system(f"multipass launch -n {mpname} -c {mpcpu} -m {mpmem} -d {mpdisk}")
        print(f"Instance {mpname} created!")
        time.sleep(3)
    else: 
        print("Going back to the main menu!") # I'll work on a fix later that allows you to either resubmit settings or go back to the main menu.
        time.sleep(3)
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
# Stop MP Instance Logic 
def stopMPI():
    print("---------------------------------------------------------------------------")
    x = subprocess.Popen("multipass list", shell=True, stdout=subprocess.PIPE)
    subprocess_return = x.stdout.read()
    print(subprocess_return.decode("ascii"))
    print("---------------------------------------------------------------------------")
    x = input(f"Please type the name of the instance you would like to stop: ")
    os.system(f"multipass stop {x}")
    print(Fore.RED)
# Delete MP Instance Logic
def deleteMPI():
    print("---------------------------------------------------------------------------")
    x = subprocess.Popen("multipass list", shell=True, stdout=subprocess.PIPE)
    subprocess_return = x.stdout.read()
    print(subprocess_return.decode("ascii"))
    print("---------------------------------------------------------------------------")
    x = input(f"Please type the name of the instance you would like to delete: ")
    os.system(f"multipass delete {x}")
    print(Fore.RED) 
# Purge MP Instance Logic
def purgeMPI():
    print("---------------------------------------------------------------------------")
    x = subprocess.Popen("multipass list", shell=True, stdout=subprocess.PIPE)
    subprocess_return = x.stdout.read()
    print(subprocess_return.decode("ascii"))
    print("---------------------------------------------------------------------------")
    x1 = input(f"This command terminates all deleted MP Instances. You cannot recover them after this process is finished. Would you like to continue? y/n?: ")
    if x1 == "y":
        print("Purging all MP Instances!")
        os.system(f"multipass purge")
        print("All deleted MP Instances have been purged.")
        time.sleep(3)
    else: 
        print("Going back to the main menu!") # I'll work on a fix later that allows you to either resubmit settings or go back to the main menu.
        time.sleep(3)
# Invoking Console
mainConsole()



