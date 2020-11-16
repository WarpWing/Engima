from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from sys import exit
import pyfiglet
import sys
import getpass
import PyInquirer
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
# PyInquirer Style Configuration 
style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

# Actual Console
console = [
    {
        'type': 'checkbox',
        'message': 'Select Multipass Options',
        'name': 'Operations',
        'choices': [
            Separator('= Basic Multipass Operations ='),
            {
                'name': 'Launch Instance'
            },
            {
                'name': 'Stop Instance'
            },
            {
                'name': 'Delete Instance'
            },
        ],
        'validate': lambda answer: 'You must choose at least one operation to do.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(console, style=style)
pprint(answers)