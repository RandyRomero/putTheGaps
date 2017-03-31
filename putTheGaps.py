#!python3

'''Program that can insert gaps into numbered files so that a new file can be added.'''

import logging, os, re

logging.basicConfig(
	format = "%(levelname) -1s %(asctime)s line %(lineno)s: %(message)s",
	level = logging.DEBUG
)

logging.disable(logging.CRITICAL)


pathToWork = ('.\\test')

def lastFileNumber(files):
	
	# Read files, check which one is last, pass number of last file to loop which start to rename files from the last one

	serialNumbers = []
	for file in files:
		if re.search(r'(\d{3})', file).group(1):
			serialNumbers.append(file)
		
	serialNumbers.sort()
	lastFile = int(re.search(r'(\d{3})', serialNumbers[len(serialNumbers) - 1]).group(1))
	logging.debug('lastFile is ' + str(lastFile))
	return lastFile
		
def rename(fileNumber, number):
	
	# The whole functuon runs like this: it takes last file (which equal length of file list), e.g. file047.txt, and rename it as file with ordered number one step higher - file048.txt. It goes from very last number to number which user chosed (inclusive).
	
	files = os.listdir(pathToWork)
	lastFile = lastFileNumber(files)
	while True:
		# print('last file is ' + str(lastFile))
		
		for i in range(lastFile, fileNumber - 1, -1): #loop runs backwards 
			
			currentFile = os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i))
			# logging.debug(currentFile)
			nextFile = os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i + number))
			try:
				os.rename(currentFile, nextFile)
				print(currentFile + ' was renamed as ' + nextFile)
				if i == fileNumber: # break while loop when for loop ended 
					return
			except FileExistsError:
				print('File already exists\n')
				lastFile = lastFileNumber(files) #TODO now it is seems redundant
				break
			except FileNotFoundError:
				print('Can\'t rename ' + currentFile + '. File is missing.')

			
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

	