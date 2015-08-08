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
import compare

# clear console
clear = lambda: os.system('cls')
clear()

# print friendly message to user
print("\n \n \t Welcome to PyMind")
print("\t Hope you'll enjoy the game")

nbTrials = 10

# generate random combinaison
random.seed();
listF = []
for x in range(0, 4):
	listF.append(random.randint(1,7))
#print(listF)

# start loop
while(nbTrials > 0):
	# get user input
	guess = input("Enter your sequence of 4 numbers. Life : " + str(nbTrials) + " \n >> ")
	# convert entry into array of integers
	print(guess)
	guess = guess.split()
	guess_int = []
	for x in guess:
		guess_int.append(int(x))
	#print(guess_int)
	res = compare.compare(guess_int, listF)
	print(res)
	if res == 1:
		print("End of Game")
		break
	else:
		print("good color : [" + str(res[0]) + "] good order : [" + str(res[1]) + "]")
		nbTrials = nbTrials - 1