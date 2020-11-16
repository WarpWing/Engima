from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pprint import pprint
import sys
from sys import exit
import getpass
import PyInquirer
import time
import pretty_errors
import os


app = 'MultipassSimplified'
username = getpass.getuser()
x = f'/home/{username}/snap/multipass'
isFile = os.path.isdir(x) 

#Multipass Install Check
def multipasscheck():
    if isFile == True: 
        pass
    else: 
        print(f"Please install Multipass before launching {app} ") 
        exit()

# Invoking Multipass Check
multipasscheck()

# Actual Console
def console():
    questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
     }
    ]
    answers = prompt(questions)
    pprint(answers)
console()