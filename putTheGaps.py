#!python3

'''Program that can insert gaps into numbered files so that a new file can be added.'''

import os, re

pathToWork = ('.\\test')


def lastFileNumber():
	while True:
		lastFile = input('Please write down number of the very file (e.g. 004): ')
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

		
def rename(number):
	
	# The whole functuon runs like this: it takes last file (which equal length of file list), e.g. file047.txt, and rename it as file with ordered number one step higher - file048.txt. It goes from very last number to number which user chosed (inclusive).
	
	files = os.listdir(pathToWork)
	lastFile = len(files)
	while True:
		# print('last file is ' + str(lastFile))
		for i in range(lastFile, number - 1, -1): #loop runs backwards 
			print('+ ' + str(i))
			try:
				os.rename(os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i)), os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i + 1)))
			except FileExistsError:
				print('File already exists\n')
				lastFile = lastFileNumber()
				break
				

########### Ask user about a number of file he wants to substitute ##########

while True:
	number = input('Where do you want to put the gap? Please write down number of file (e.g. 004) which do you want to substitute: ')
	if re.search(r'^\d{3}$', number): # only three digits
		if os.path.exists(os.path.join(pathToWork, 'file{0:0>3}.txt'.format(number))): # check if file with this number exists
			print('This file exists. Accepted.')
			rename(int(number))
			break
		else:	
			print('file{0:0>3}.txt doesn\'t exists. Choose another one.\n'.format(number))
			continue
	else:
		print('Incorrect input. Try again.\n')
		continue

