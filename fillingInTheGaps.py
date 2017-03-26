#! python3


'''Program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.'''
import os

pathToWork = ('.\\test')
files = os.listdir(pathToWork)
allesGut = True

# look for missing files
for i in range(1, len(files) + 1):
	currentFile = os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i))
	if not os.path.exists(currentFile):
		print('file{0:0>3}.txt is missing!'.format(i))
		allesGut = False
		y = 1

		while True:
			#loop recusively looks for file with next number and renames it as missing file

			nextFile = os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i + y))
			
			if os.path.exists(nextFile):
				#if file exists - rename it
				os.rename(nextFile, currentFile)
				print(os.path.basename(nextFile) + ' was renamed to ' + os.path.basename(currentFile))
				break
			else:
				# if file doesn't exist - increment 'y' in order to look for the file with bigger ordinal number next time
				if not y > len(files):
					y += 1
					continue
				else:
					print('There are no files to rename anymore')
					break
	
if allesGut:
	print('All files are there.')
