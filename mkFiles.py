#!python3

#nano script that creates files with indexes through loop

import os

pathToWork = ('.\\test') 

while True:
	quantity = input('How many files do you want to create? Choose between 1 and 100: ')
	quantity = int(quantity)
	if quantity >= 1 and quantity <= 100:
		print('Ok, there will be ' + str(quantity) + ' files.')
		break
	else:
		print('Try again')
		continue

for i in range(1, quantity + 1): # to start with 1 and to end with 100
		newFile = open('.\\test\\file{0:0>3}.txt'.format(i), 'w') 
		# {0:0>3} .format(i)- all of this is needed to print out numbers with leading zeros . 3 is width, > is right align, 0 - is filler, 0: - I couldn't figure out
		newFile.close()

print(str(quantity) + ' files were successfully created.')		