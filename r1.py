#!/usr/bin/env python

from operator import itemgetter
import sys

wordBefore = None
traffic_num = 0
j = 0

# input comes from STDIN
for line in sys.stdin:
	words = line.split(',')
	#for i in range(len(words)):
		#print(words[i])
	
	'''Si el nombre de la calle es diferente'''
	if(words[0] != str(wordBefore)):
		print(str(wordBefore) + ':' + str(traffic_num))
		'''Nos saltamos la primera iteracion porque todavia no tenemos ninguna 
		calle anterior guardada'''
		if(j > 0):
			'''Reiniciamos el calculo para la calle siguiente'''
			traffic_num = 0
		j = j + 1
	
	'''Recorremos la tupla por columnas'''
	for i in range(len(words)):
		'''Nos saltamos la primera columna porque tiene string'''
		if(i > 0):
			'''Vamos sumando el trafico de cada horario'''
			traffic_num += float(words[i].replace('[','').replace(']','')
			.replace('\'','').replace('\\','').replace('n',''))
		#print(traffic_num)
	
	'''Guardamos la calle actual en la calle anterior'''
	wordBefore = words[0]

print(str(wordBefore) + ':' + str(traffic_num))
