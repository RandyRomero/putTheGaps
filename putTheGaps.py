#!python3

'''Program that can insert gaps into numbered files so that a new file can be added.'''

import os, re

pathToWork = ('.\\test')

########### Ask user about a number of file he wants to substitute ##########

while True:
	number = input('Where do you want to put the gap? Please write down number of file (e.g. 004) which do you want to substitute: ')
	if re.search(r'^\d{3}$', number): # only three digits
		if os.path.exists(os.path.join(pathToWork, 'file{0:0>3}.txt'.format(number))): # check if file with this number exists
			print('This file exists. Accepted.')
			break
		else:	
			print('file{0:0>3}.txt doesn\'t exists. Choose another one.\n'.format(number))
			continue
	else:
		print('Incorrect input. Try again.\n')
		continue

