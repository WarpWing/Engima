import getpass
import PyInquirer
import time
import pretty_errors
import os
from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint

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

os.system('clear')
multipasscheck()
time.sleep(2)
def console():
    