#!/usr/bin/env python

import operator
from operator import itemgetter
import sys

header = ['12:00-1:00 AM', '1:00-2:00AM', '2:00-3:00AM', '3:00-4:00AM', '4:00-5:00AM', '5:00-6:00AM', '6:00-7:00AM', '7:00-8:00AM', '8:00-9:00AM', '9:00-10:00AM', '10:00-11:00AM', '11:00-12:00PM', '12:00-1:00PM', '1:00-2:00PM', '2:00-3:00PM', '3:00-4:00PM', '4:00-5:00PM', '5:00-6:00PM', '6:00-7:00PM', '7:00-8:00PM', '8:00-9:00PM', '9:00-10:00PM', '10:00-11:00PM', '11:00-12:00AM']
row = 0
wordBefore = None
streets = []
traffic_in_street  = []  # List for storing the traffic per hour in a street
traffic_per_street = []  # List for storing the max traffic per hour in a street
# input comes from STDIN
for line in sys.stdin:
	#print("Row: " + str(row))
	# Convert ['123', '234', '345'] to 123, 234, 345
	for i in range(len(line)):
		newLine = line.replace("'", "").replace("[", "").replace("]", "")

	# Split by comma
	words = newLine.split(",")
	#print(words)
	
	if(row == 0):
		print(words[0])
	
	elif(words[0] != str(wordBefore)):
		#print("Cambio de " + str(wordBefore)+ " a " + str(words[0]))
		#print(words)
		if(wordBefore != None):
			traffic_per_street.append(max(enumerate(traffic_in_street), key=operator.itemgetter(1)))  # Choose the greatest one
		traffic_in_street  = [0.0] * (len(words[5:31]))
		for j in range(len(words[5:31])):
			#(words[j + 5])
			traffic_in_street[j] = traffic_in_street[j] + float(words[j + 5]) # Each hour correspond to a position in the array
		streets.append(words[0])  # Add columns
		wordBefore = words[0]
	else:
		for j in range(len(words[5:31])):
			# print(words[j + 5])
			traffic_in_street[j] = traffic_in_street[j] + float(words[j + 5]) # Each hour correspond to a position in the array
	
		#print(traffic_in_street)		
		#print(traffic_per_street)

	row = row + 1

for j in range(len(words[5:31])):
	#(words[j + 5])
	traffic_in_street[j] = traffic_in_street[j] + float(words[j + 5]) # Each hour correspond to a position in the array
	traffic_per_street.append(max(enumerate(traffic_in_street), key=operator.itemgetter(1)))  # Choose the greatest one


#print(streets)
#print(header)
#print(traffic_per_street)

for k in range(len(streets)):
	print(str(streets[k]) + ": " + str(header[traffic_per_street[k][0]]))  # Final results

