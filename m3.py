#!/usr/bin/env python

import sys
import re

j = 0
# input comes from STDIN (standard input)
for line in sys.stdin:
	i = 0 # Number of words that has been processed
	# split the line into words
	words = line.split(",")

	# Check if the line has a different number of attributes (in this case, 31)
	# If that occurs, skip the line
	if(len(words) != 31):
		#print("Different number of attributes in line " + str(j))
		j = j + 1
		continue

	# Check if any of the words in the line that should not contain any string, contains one
	# If that occurs, skip the line	
	r = re.compile("[a-zA-Z]")
	result1 = filter(r.match, str(words[0:2]))
	result2 = filter(r.match, str(words[7:30]))
	if((result1 != "" or result2 != "") and j != 0):
		#print("Fila " + str(j) + " contiene string sin deberlo")
		j = j + 1
		continue
	
	for i in range(len(words)):
		if(words[i] != words[i].strip(' ')):
			#print("Spaces in line" + str(j) + ":" + words[i])
			words[i] = words[i].strip(' ')
			continue

	# Delete any leading or trailing whitspace in the words of the line
	newList = []
	if(j > 0):
		newList.append(words[2])
		newList.append(words[7:31])
	print(str(newList))

	j = j + 1
