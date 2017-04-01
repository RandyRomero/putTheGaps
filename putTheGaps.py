#!python3

'''Program that can insert gaps into numbered files so that a new file can be added.'''

import logging, os, re, sys

logging.basicConfig(
	format = "%(levelname) -1s %(asctime)s line %(lineno)s: %(message)s",
	level = logging.DEBUG
)

logging.disable(logging.CRITICAL)
pathToWork = ('.\\test')
files = os.listdir(pathToWork)

def lastFileNumber():
	
	# Read files, check which one is last, pass number of last file to loop which start to rename files from the last one

	serialNumbers = []
	for file in files:
		if re.search(r'(\d{3})', file).group(1):
			serialNumbers.append(file)
		
	serialNumbers.sort()
	lastFile = int(re.search(r'(\d{3})', serialNumbers[len(serialNumbers) - 1]).group(1))
	logging.debug('lastFile is ' + str(lastFile))
	return lastFile

def checkAllFilesThere():
	for i in range(fileNumber, fileNumber + gapSize):
		currentFile = 'file{0:0>3}.txt'.format(i)
		if not os.path.exists(os.path.join(pathToWork, currentFile)):
			print('Error: there are some files missing(' + currentFile + '). Can\'t rename missing file. Quit.')
			sys.exit()
		
def rename():
	
	# The whole functuon runs like this: it takes last file (which equal length of file list), e.g. file047.txt, and rename it as file with ordered number one step higher - file048.txt. It goes from very last number to number which user chosed (inclusive).
	
	
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
				break
			except FileNotFoundError:
				print('Can\'t rename ' + currentFile + '. File is missing.')

############################################################################

lastFile = lastFileNumber()

########### Ask user about a number of file he wants to substitute ##########

while True:
	fileNumber = input('Where do you want to put the gap? Please write down first number of file (e.g. 004) which do you want to substitute: ')
	if re.search(r'^\d{3}$', fileNumber): # only three digits
		if os.path.exists(os.path.join(pathToWork, 'file{0:0>3}.txt'.format(fileNumber))): # check if file with this number exists
			fileNumber = int(fileNumber)
			print('This file exists. Accepted.')
			break
		else:	
			print('file{0:0>3}.txt doesn\'t exists. Choose another one.\n'.format(fileNumber))
			continue
	else:
		print('Incorrect input. Try again.\n')
		continue

while True:
	gapSize = input('How big should be the gap? Please write down a number (1 or 2 digit): ')
	if re.search(r'^\d|\d\d$', gapSize):
		gapSize = int(gapSize)
		print('Number accepted')
		checkAllFilesThere()
		rename()
		break
	else:
		print('Input error. Try something else')
		continue

	