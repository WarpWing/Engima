import sys
import getpass
import time
import pretty_errors
import os

# File Wide Variables
app = 'MultipassSimplified'
username = getpass.getuser()
m = f'/home/{username}/snap/multipass'  # macOS
w = f"c:/Program Files/multipass"       # Windows
isFile = os.path.isdir(w) 

#Multipass Install Check
def multipassCheck():
    if isFile: 
        pass
    else: 
        print(f"Please install Multipass before launching {app} ") 
        exit()

# MPS Console Logic     
options = {
    "1" : "Launch Instance with Parameters",
    "2" : "Stop Instance with Parameters"
}
def mainConsole():
    i = input("Enter Your Input: ")
    try:
        print(options[i])
    except KeyError:
        print("Invalid Operation!")

     
        
# Invoking Multipass Check
print(getpass.getuser())
multipassCheck() 
# Invoke Console
mainConsole()
