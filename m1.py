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
		print("Different number of attributes in line " + str(j))
		j = j + 1
		continue;
	
	r = re.compile("[a-zA-Z]")
	result1 = filter(r.match, str(words[0:2]))
	result2 = filter(r.match, str(words[7:30]))
	if((result1 != "" or result2 != "") and j != 0):
		print("Fila " + str(j) + " contiene string sin deberlo")
		continue;

	# print(str(j) + str(words))

	j = j + 1

