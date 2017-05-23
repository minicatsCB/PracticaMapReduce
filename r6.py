#!/usr/bin/env python

import operator
from operator import itemgetter
import sys

row = 0
wordBefore = None
streets = []
header = []
traffic_per_hours_in_street = []  # List for storing the traffic each hour in each street
traffic_in_street  = []  # List for storing the traffic per hour in a street
traffic_per_street = []  # List for storing the max traffic per hour in a street
incoming_street = 0;
save_header = True
# input comes from STDIN
for line in sys.stdin:
	#print("Row: " + str(row))
	# Convert ['123', '234', '345'] to 123, 234, 345
	for i in range(len(line)):
		newLine = line.replace("'", "").replace("[", "").replace("]", "")

	# Split by comma
	words = newLine.split(",")
	#print(words)
	
	# Execute only once at the beginning
	if(save_header == True):
		header = words[5:31]
		save_header = False
	
	# First, check if we are in Broadway street
	if(words[0].lower() == "broadway"):
		# If change
		if(words[1] != str(wordBefore)):
			print("Cambiando de " + str(wordBefore) + " a " + str(words[1]))
			#print(words[0:2])
			if(wordBefore != None):
				traffic_per_hours_in_street.append(traffic_in_street)
			#print("\nTotal traffic in a street (by index)" + str(traffic_per_hours_in_street))
			traffic_in_street  = [0.0] * (len(words[5:31]))
			for j in range(len(words[5:31])):
				#(words[j + 5])
				traffic_in_street[j] = traffic_in_street[j] + float(words[j + 5]) # Each hour correspond to a position in the array
			streets.append(words[1])  # Add columns
			wordBefore = words[1]
		else:
			# Calculate the total traffic per incoming street
			for j in range(len(words[5:31])):
				# print(words[j + 5])
				traffic_in_street[j] = traffic_in_street[j] + float(words[j + 5]) # Each hour correspond to a position in the array
			#print("Traffic in street: " + str(traffic_in_street))

		row = row + 1

for j in range(len(words[5:31])):
	# print(words[j + 5])
	traffic_in_street[j] = traffic_in_street[j] + float(words[j + 5]) # Each hour correspond to a position in the array
traffic_per_hours_in_street.append(traffic_in_street)
		
	
'''	
	elif(words[0] != str(wordBefore)):
		#print("Cambio de " + str(wordBefore) + " a " + str(words[0]))
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

'''
#print(streets)
#print("Heeeeeader: " + str(header))
#print(traffic_per_street)
print("-----------------------------------------------\n")
for i in range(len(traffic_per_hours_in_street)):
	print("\nTotal traffic in a street (by index)" + str(traffic_per_hours_in_street[i]))
print("-----------------------------------------------\n")

# Get the greatest value for each hour
#a = [[1,7,2],[5,8,4],[6,3,9]]
numbers_in_col = [] # Coge los todos los numero de una columna
max_value = [] # Guada el valor maximo de cada columna, junto con sus coordenadas en la lista a

# Cada columna es una hora
# Cada fila es una calle
# Buscamos la mayor "fila" en cada columna, esto es, el mayor trafico por calle (fila) en cada hora (columna)
# Miramos columna a columna, sacando el mayor valor
# Damos tantas vueltas como columnas haya (suponemos que la matriz es cuadrada)
for col in range(len(traffic_per_hours_in_street[0])):  # len = 15
	numbers_in_col = []
	for row in range(len(traffic_per_hours_in_street)):  # len(a) = 15
		# Me guardo los elementos de [][0]...[][n] cada vez
		numbers_in_col.append(traffic_per_hours_in_street[row][col])
	# De ahi calculo el maximo y guardo sus coordenadas
	b = max(enumerate(numbers_in_col), key=operator.itemgetter(1))
	max_value.extend([b[1], b[0], col])

print(max_value)

#print("Numero horas: " + str(len(traffic_per_hours_in_street[0])))
#print("Numero original horas: " + str(len(header)))
#print("Numero calles: " + str(len(traffic_per_hours_in_street)))
#print("Numero original calles: " + str(len(streets)))

for k in range(len(max_value)):
	# Cada 3 elementos es un trio (valor,row,col)
	if(k%3 == 0):  # len(a[0]) = 3
		print("Max value of column " + str(k/3) + ": " + str(max_value[k]) + " (at index [" + str(max_value[k + 1]) +"][" + str(max_value[k + 2]) + "])")

print("\n")
print(header)
for k in range(len(max_value)):
	# Cada 3 elementos es un trio (valor,row,col)
	if(k%3 == 0):  # len = 15
		print(max_value[k + 1])
		#print("Max value of column " + str(k/3) + ": " + str(max_value[k]) + " (at index [" + str(max_value[k + 1]) +"][" + header[max_value[k + 2]] + "])")
		print("Max street of hour " + header[max_value[k + 2]] + ": " + streets[max_value[k + 1]])


