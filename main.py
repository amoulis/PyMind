""" PyMind is inspired by the 'mastermind' game.
- 8 colors, here replaced by numbers from 1 to 7.
- The player needs to guess a 4 color combinaison (that would be generated randomly)
- After each trial the player knows the number
Mastermind was invented by Mordecai Meirowitz in 1970

PyMind works with was developped and tested with Python3.4
"""

import sys
import os
import random

# clear console
clear = lambda: os.system('cls')
clear()

# print friendly message to user
print("\n \n \t Welcome to PyMind")
print("\t Hope you'll enjoy the game")

nbTrials = 10

# generate random combinaison
random.seed();
list = []
for x in range(0, 4):
	list.append(random.randint(1,7))
#print(list)

# start loop
while(nbTrials > 0):
	print("in loop")

# analyze player's n-th guess

# assert results (number of color well placed, misplaced)
