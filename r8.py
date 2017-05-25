#!/usr/bin/env python

from operator import itemgetter
import sys

wordBefore = None
wordBeforeTo = None
traffic_num = 0
j = 0
most_traffic_street = None
most_traffic = 0

# input comes from STDIN
for line in sys.stdin:
	words = line.split(',')

	if(str(words[0]) != str(wordBefore)):
		if(str(words[1:2]) != str(wordBeforeTo)):
			print("Sentido con mas trafico: " + str(most_traffic_street))
			print("Trafico de " + str(wordBefore).replace('[','') + "-" + str(most_traffic_street) + ":" + str(most_traffic))
			print("----------------------------------------------------------------------------")
			'''Reiniciamos la variable para comparar los valores del trafico'''	
			most_traffic = 0
		print("Calle: " + str(words[0]).replace('[',''))
		
	'''Si el nombre de la calle de sentido es diferente al anterior'''
	if(str(words[1:2]) != str(wordBeforeTo)):
		'''Recorremos la calles a las que se dirige'''
		if(traffic_num > most_traffic):
			'''Guardamos el nombre de la calle y el trafico en dicho tramo'''
			most_traffic = traffic_num
			most_traffic_street = str(words[1:2]).replace('[','').replace(']','').replace('"','')
		'''Reiniciamos el calculo para la calle siguiente'''
		traffic_num = 0
		

	'''Recorremos la tupla por columnas'''
	for i in range(len(words)):
		'''Nos saltamos las 2 primeras columnas porque tienen string'''
		if(i > 1):
			'''Vamos sumando el trafico de cada horario'''
			traffic_num += float(words[i].replace('[','').replace(']','')
			.replace('\'','').replace('\\','').replace('n',''))
		#print(traffic_num)

	'''Guardamos la calle actual en la calle anterior'''
	wordBefore = words[0]
	'''Guardamos la calle de sentido actual en la calle de sentido anterior'''
	wordBeforeTo = str(words[1:2])
	'''Incrementamos el valor de la iteracion'''
	j = j + 1

print("Sentido con mas trafico: " + str(most_traffic_street))
print("Trafico de " + str(wordBefore).replace('[','') + "-" + str(most_traffic_street) + ":" + str(most_traffic))
print("----------------------------------------------------------------------------")
