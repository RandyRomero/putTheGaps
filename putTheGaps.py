#!python3

'''Program that can insert gaps into numbered files so that a new file can be added.'''

import os, re

pathToWork = ('.\\test')


def lastFileNumber():
	while True:
		lastFile = input('Please write down number of the very last file (e.g. 004): ')
		if re.search(r'^\d{3}$', lastFile): # only three digits
			if os.path.exists(os.path.join(pathToWork, 'file{0:0>3}.txt'.format(lastFile))): # check if file with this number exists
				print('This file exists. Accepted.')
				return int(lastFile)
			else:	
				print('file{0:0>3}.txt doesn\'t exists. Choose another one.\n'.format(lastFile))
				continue
		else:
			print('Incorrect input. Try again.\n')
			continue

		
def rename(fileNumber, number):
	
	# The whole functuon runs like this: it takes last file (which equal length of file list), e.g. file047.txt, and rename it as file with ordered number one step higher - file048.txt. It goes from very last number to number which user chosed (inclusive).
	
	files = os.listdir(pathToWork)
	lastFile = len(files)
	end = False
	while end == False:
		# print('last file is ' + str(lastFile))
		
		for i in range(lastFile, fileNumber - 1, -1): #loop runs backwards 
			
			currentFile = os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i))
			nextFile = os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i + number))
			try:
				os.rename(currentFile, nextFile)
				print(currentFile + ' was renamed as ' + nextFile)
				if i == fileNumber: # break while loop when for loop ended 
					return
			except FileExistsError:
				print('File already exists\n')
				lastFile = lastFileNumber()
				break
			
				
########### Ask user about a number of file he wants to substitute ##########

while True:
	fileNumber = input('Where do you want to put the gap? Please write down first number of file (e.g. 004) which do you want to substitute: ')
	if re.search(r'^\d{3}$', fileNumber): # only three digits
		if os.path.exists(os.path.join(pathToWork, 'file{0:0>3}.txt'.format(fileNumber))): # check if file with this number exists
			print('This file exists. Accepted.')
			break
		else:	
			print('file{0:0>3}.txt doesn\'t exists. Choose another one.\n'.format(fileNumber))
			continue
	else:
		print('Incorrect input. Try again.\n')
		continue

while True:
	number = input('How big should be the gap? Please write down a number (1 or 2 digit): ')
	if re.search(r'^\d|\d\d$', number):
		print('Number accepted')
		rename(int(fileNumber), int(number))
		break
	else:
		print('Input error. Try something else')
		continue

	