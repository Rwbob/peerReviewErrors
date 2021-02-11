# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Robert Sivadon
# Creation Date: 02/14/2021
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''\nYou are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. In the other cave 
the dragon is greedy and hungry, and will eat you on sight.''') # style fix, prints without indents, added additional text and empty line at begining to enhance readability 
	print()

def chooseCave():
	cave = '' # 1) fixed indent error 
	if cave != '1' or cave != '2': # 2) changed to conditional rather than infinite loop --- 3) changed to an 'OR' statement 
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return cave # 4) fixed misspelling error; caves to cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2) # 5) fixed time amount according to comment 
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!') # 6) added missing parenthesis  

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y': # 7) added missing '=' 
	displayIntro()
	chosenCave = chooseCave() # 8) fixed call to chooseCave() and changed variable to remain consistant to checkCave(chosenCave)
	checkCave(chosenCave)
    
	print('Do you want to play again? (yes or no)') 
	playAgain = input()
	if playAgain == "no" or playAgain == 'n': # 9) added additional paramater to stay consistant with above condition that sets PlayAgain flag.  
		print("Thanks for playing") # 10) fixed spelling error; planing to playing 