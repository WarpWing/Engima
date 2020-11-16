import getpass
import pretty_errors
import os

app = 'MultipassSimplified'
#Multipass Install Check
username = getpass.getuser()
x = f'/home/{username}/snap/multipass'
isFile = os.path.isdir(x) 

if isFile == True: 
    print(f"Multipass is installed! Loading up {app}")
else: 
    print(f"Please install Multipass before launching {app} ") 
