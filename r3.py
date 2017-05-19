#!/usr/bin/env python

from operator import itemgetter
import sys

traffic = []
streets = []
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

	'''Si el nombre de la calle es diferente'''
	if(words[0] != str(wordBefore)):
		#print(words[0] + ':' + str(wordBefore))
		'''Guardamos el nombre de la calle a la lista de calles'''
		streets.append(words[0])
		'''Nos saltamos la primera iteracion porque todavia no tenemos ninguna 
		calle anterior guardada'''
		if(j > 0):
			'''Guardamos trafico calculado en la lista de traficos'''
			traffic.append(traffic_num)
			'''Reiniciamos el calculo para la calle siguiente'''
			traffic_num = 0
		j = j + 1
	
	'''Recorremos la tupla por columnas'''
	for i in range(len(words)):
		'''Nos saltamos las 2 primeras columnas que tienen strings'''
		if(i > 0):
			'''Vamos sumando el trafico de cada horario'''
			traffic_num += float(words[i].replace('[','').replace(']','')
			.replace('\'','').replace('\\','').replace('n',''))
		#print(traffic_num)
	
	'''Guardamos la calle actual en la calle anterior'''
	wordBefore = words[0]

'''Recorremos la lista de traficos'''
for i in range(len(traffic)):
	'''Si el trafico actual es mayor que trafico mas alto hasta el momento'''
	if(traffic[i] > most_traffic_num):
		'''Guardamos el nombre de la calle'''
		most_traffic_street = streets[i]
		'''Guardamos el numero de trafico'''
		most_traffic_num = traffic[i]
	'''Vamos acumulando el trafico de cada calle en una variable'''
	traffic_total += traffic[i]

print("Trafico total:" + str(traffic_total))
print("Calle con mas trafico:" + most_traffic_street.replace('[',''))
print("Numero mayor de trafico en una calle:" + str(most_traffic_num))
