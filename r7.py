#!/usr/bin/env python

from operator import itemgetter
import sys

from_traffic = []
to_traffic = []
traffic_num = 0
from_traffic_total = 0
to_traffic_total = 0

# input comes from STDIN
for line in sys.stdin:
	words = line.split(',')
	#for i in range(len(words)):
		#print(words)
	#street = str(words[1:2]).replace('[','').replace(']','').replace('"','').replace(' ','')

	'''Buscamos las tuplas con calles dirigidas a Broadway'''
	if(str(words[1:2]).replace('[','').replace(']','')
		.replace('"','').replace('\'','').replace(' ','') == 'BROADWAY'):
		'''Recorremos la tupla por columnas'''
		for i in range(len(words)):
			'''Nos saltamos las 2 primeras columnas que tienen strings'''
			if(i > 1):
				'''Vamos sumando el trafico de cada horario'''
				traffic_num += float(words[i].replace('[','').replace(']','')
				.replace('\'','').replace('\\','').replace('n',''))		

		'''Guardamos trafico calculado en la lista de traficos'''
		to_traffic.append(traffic_num)
		'''Reiniciamos el calculo para la calle siguiente'''
		traffic_num = 0

	'''Buscamos las tuplas con calles que salen de Broadway'''
	if(words[0].replace('[','').replace('\'','') == 'BROADWAY'):
		'''Recorremos la tupla por columnas'''
		for i in range(len(words)):
			'''Nos saltamos las 2 primeras columnas que tienen strings'''
			if(i > 1):
				'''Vamos sumando el trafico de cada horario'''
				traffic_num += float(words[i].replace('[','').replace(']','')
				.replace('\'','').replace('\\','').replace('n',''))
		
		'''Guardamos trafico calculado en la lista de traficos'''
		from_traffic.append(traffic_num)
		'''Reiniciamos el calculo para la calle siguiente'''
		traffic_num = 0

'''Recorremos la lista de traficos que salen de Broadway'''
for i in range(len(from_traffic)):
	'''Vamos acumulando el trafico de cada calle en una variable'''
	from_traffic_total += from_traffic[i]

'''Recorremos la lista de traficos que llegan a Broadway'''
for i in range(len(to_traffic)):
	'''Vamos acumulando el trafico de cada calle en una variable'''
	to_traffic_total += to_traffic[i]

print("Trafico total de salida:" + str(from_traffic_total))
print("Trafico total de entrada:" + str(to_traffic_total))
print("Diferencia de trafico:" + str(abs(to_traffic_total - from_traffic_total)))

