import getpass
import pretty_errors
import os

app = 'MultipassSimplified'
username = getpass.getuser()
x = f'/home/{username}/snap/multipass'
isFile = os.path.isdir(x) 

#Multipass Install Check
def multipasscheck():
    if isFile == True: 
        print(f"Multipass is installed! Loading up {app}")
    else: 
        print(f"Please install Multipass before launching {app} ") 

multipasscheck()