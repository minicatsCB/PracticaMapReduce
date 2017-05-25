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
	is_float = re.findall("\d+\.\d+", str(words[7:30]))
	if(((result1 != "" or result2 != "") or not(not is_float)) and j != 0):  # First line does not count
		#print("Fila " + str(j) + " contiene string o float sin deberlo")
		j = j + 1
		continue
	
	# Delete any leading or trailing whitspace in the words of the line
	for i in range(len(words)):
		if(words[i] != words[i].strip(' ')):
			#print("Spaces in line" + str(j) + ":" + word)
			words[i] = words[i].strip(' ')
			continue

	#print(str(j) + str(words))  # Print line number and line content
	# 31 and no 30, because of the \n character
	words[7:31] = map(lambda s: s.strip(), words[7:31])  # Delete carriage return
	print(words[7:31])

	j = j + 1

