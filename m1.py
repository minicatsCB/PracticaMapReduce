#!/usr/bin/env python

import sys

j = 0
# input comes from STDIN (standard input)
for line in sys.stdin:
	# split the line into words
	words = line.split(",")

	# Check if the line has a different number of attributes (in this case, 31)
	# If that occurs, skip the line
	if(len(words) != 31):
		print("Different number of attributes in line " + str(j))
		j = j + 1
		continue;

	# increase counters
	i = 0 # Number of words that has been processed
	for word in words:
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#print("---------------------------- Palabra " + str(i) + " ------------------------")
		#print '%s' % (word)
		if(i == 30):
			#print("--- Linea " + str(j) + " ---")
			pass
		i = i + 1
	j = j + 1

