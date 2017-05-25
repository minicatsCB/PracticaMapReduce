#!/usr/bin/env python

from operator import itemgetter
import sys

'''
	Trying to do this:

	     sumCol0    sumCol1   sumCol2    sumCol3  sumColn  sumCol30
	       |          |          |          |        |        |
	-----------------------------------------------------------------
	|    col0   |   col1   |   col2   |   col3   | coln |   col30   |
	-----------------------------------------------------------------
	'''

header = ['12:00-1:00 AM', '1:00-2:00AM', '2:00-3:00AM', '3:00-4:00AM', '4:00-5:00AM', '5:00-6:00AM', '6:00-7:00AM', '7:00-8:00AM', '8:00-9:00AM', '9:00-10:00AM', '10:00-11:00AM', '11:00-12:00PM', '12:00-1:00PM', '1:00-2:00PM', '2:00-3:00PM', '3:00-4:00PM', '4:00-5:00PM', '5:00-6:00PM', '6:00-7:00PM', '7:00-8:00PM', '8:00-9:00PM', '9:00-10:00PM', '10:00-11:00PM', '11:00-12:00AM']
lst = [0.0] * (len(header))  # Results of different columns
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
	
	if(row != 0 and not(words[0] == "12:00-1:00 AM")):
		for i in range(len(words)):
			lst[i] = lst[i] + float(words[i])  # Add the entire column

	row = row + 1

for j in range(len(words)):
	lst[j] = lst[j] / float((row))  # Calculate average

for k in range(len(words)):
	print(str(header[k]) + ": " + str(int(lst[k]))) + " cars/hour" # Final results

