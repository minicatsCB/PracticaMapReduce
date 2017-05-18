#!/usr/bin/env python

from operator import itemgetter
import sys

row = 0
# input comes from STDIN
for line in sys.stdin:
	#print("Row: " + str(row))
	# Convert ['123', '234', '345'] to 123, 234, 345
	for i in range(len(line)):
		newLine = line.replace("'", "").replace("[", "").replace("]", "")

	# Split by comma
	words = newLine.split(",")
	#print(words)
	
	# Maybe this is not necessary because there is only one iteration through all the rows 
	if(row == 0):
		lst = [0.0] * (len(words))  # Empty list for storing the results of different columns
		header = [""] * (len(words))  # Empty list for storing the names of different columns
		for x in range(len(words)):
					header[x] = header[x] + words[x]  # Add columns
	else:	
		for i in range(len(words)):
			lst[i] = lst[i] + float(words[i])  # Add

	row = row + 1

for j in range(len(words)):
	lst[j] = lst[j] / float((row))  # Average

header = map(lambda s: s.strip(), header)  # Delete header carrage return
for k in range(len(words)):
	print(str(header[k]) + ": " + str(lst[k])) # Final results

	'''
	Trying to do this:

	     sumCol0    sumCol1   sumCol2    sumCol3  sumColn  sumCol30
	       |          |          |          |        |        |
	-----------------------------------------------------------------
	|    col0   |   col1   |   col2   |   col3   | coln |   col30   |
	-----------------------------------------------------------------
	'''

