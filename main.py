import sys
import getpass
import time
import pretty_errors
import os

# File Wide Variables
app = 'MultipassSimplified'
username = getpass.getuser()
x = f'/home/{username}/snap/multipass'
isFile = os.path.isdir(x) 

#Multipass Install Check
def multipasscheck():
    if isFile: 
        pass
    else: 
        print(f"Please install Multipass before launching {app} ") 
        exit()

# Invoking Multipass Check
multipasscheck()

