#!/usr/bin/env python

from operator import itemgetter
import sys

row = 0
# input comes from STDIN
for line in sys.stdin:
	print("Row: " + str(row))
	# Convert ['123', '234', '345'] to 123, 234, 345
	for i in range(len(line)):
		newLine = line.replace("'", "").replace("[", "").replace("]", "")

	# Split by comma
	words = newLine.split(",")
	#print(words)
	
	# Maybe this is not necessary because there is only one iteration through all the rows 
	if(row == 0):
		lst = [0] * (len(words))  # Empty list for storing the results of differents columns
	else:	
		for i in range(len(words)):
			lst[i] = lst[i] + int(words[i])

	print(lst)

	'''
	Trying to do this:

	     sumCol0    sumCol1   sumCol2    sumCol3  sumColn  sumCol30
	       |          |          |          |        |        |
	-----------------------------------------------------------------
	|    col0   |   col1   |   col2   |   col3   | coln |   col30   |
	-----------------------------------------------------------------
	'''

	row = row + 1


