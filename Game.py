import numpy as np
from numpy import random

items=['Stone','Paper','Scissor']
computer_choice=np.random.choice(items)


if computer_choice=='Stone':
    comp='Stone'
if computer_choice=='Paper':
    comp='Paper'
if computer_choice=='Scissor':
    comp='Scissor'
you=input('Enter the choice you want : \n')  

def game(comp,you):
    if comp==you:
        print('Draw')
    if comp=='Stone':
        if you=='Paper':
            print('You Win')
        elif you=='Scissor':
            print('You Loss')
    if comp=='Paper':
        if you=='Scissor':
            print('You Win')
        elif you=='Stone':
            print('You Loss')        
    if comp=='Scissor':
        if you=='Stone':
            print('You Win')
        elif you=='Paper':
            print('You Loss')        
game(comp,you)
print(computer_choice)