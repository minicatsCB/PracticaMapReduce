#!/usr/bin/env python

from operator import itemgetter
import sys

traffic = []
cities = []
numbers = []
wordBefore = None
traffic_num = 0
most_traffic_street = None
most_traffic_num = 0
traffic_total = 0
j = 0

# input comes from STDIN
for line in sys.stdin:
	words = line.split(',')
	#for i in range(len(words)):
		#print(words[i])

	if(words[0] != str(wordBefore)):
		#print(words[0] + ':' + str(wordBefore))
		cities.append(words[0])
		if(j > 0):
			traffic.append(traffic_num)
			traffic_num = 0
		j = j + 1
	
	for i in range(len(words)):
		if(i > 0):
			traffic_num += float(words[i].replace('[','').replace(']','')
			.replace('\'','').replace('\\','').replace('n',''))
		#print(traffic_num)
		
	wordBefore = words[0]

for i in range(len(traffic)):
	if(traffic[i] > most_traffic_num):
		most_traffic_street = cities[i]
		most_traffic_num = traffic[i]
	traffic_total += traffic[i]

print("Trafico total:" + str(traffic_total))
print("Calle con mas trafico:" + most_traffic_street.replace('[',''))
print("Numero mayor de trafico en una calle:" + str(most_traffic_num))
