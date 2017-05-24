#!/usr/bin/env python

from operator import itemgetter
import sys


streets = []
streetsToTmp = []
streetsTo = []
trafficToTmp = []
trafficTo = []
traffic = []
wordBefore = None
wordBeforeTo = None
traffic_num = 0
j = 0
most_traffic_street = None
most_traffic = 0

# input comes from STDIN
for line in sys.stdin:
	words = line.split(',')

	'''Si el nombre de la calle de sentido es diferente al anterior'''
	if(str(words[1:2]) != str(wordBeforeTo)):
		'''Nos saltamos las 2 primeras iteraciones porque todavia no tenemos ninguna 
		calle de sentido anterior guardada'''
		if(j > 1):
			'''Guardamos el nombre de la calle en la lista de calles de sentido'''
			streetsToTmp.append(wordBeforeTo)
			'''Nos saltamos las 3 primeras iteraciones porque todavia no tenemos calculado 
			el trafico entre dos calles'''
			if(j > 2):
				'''Guardamos trafico calculado en una lista temporal 
				de traficos para esa calle'''
				trafficToTmp.append(traffic_num)
				'''Reiniciamos el calculo para la calle siguiente'''
				traffic_num = 0
		'''Si el nombre de la calle es diferente'''
		if(words[0] != str(wordBefore)):
			'''Nos saltamos la primera iteracion porque todavia no tenemos ninguna 
			calle anterior guardada'''
			if(j > 0):
				'''Guardamos el nombre de la calle a la lista de calles'''
				streets.append(words[0])
				'''Nos saltamos la primera iteracion porque todavia no tenemos ninguna 
				calle de sentido guardada'''
				if(j > 1):
					'''Guardamos la lista temporal de calles en sentido a otra'''
					streetsTo.append(streetsToTmp)
					'''Guardamos la lista temporal de traficos en otra lista'''
					trafficTo.append(trafficToTmp)
					'''Vaciamos las listas temporales'''
					streetsToTmp = []
					trafficToTmp = []
			

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


#for i in range(len(streets) - 1):
	#print("Calle: " + str(streets[i]).replace('[',''))
	#print("Sentidos: ")
	#for j in range(len(streetsTo[i])):		
		#print(str(streetsTo[i][j]) + ":" + str(trafficTo[i][j]))

'''Por cada calle'''
for i in range(len(streets) - 1):
	street = str(streets[i]).replace('[','')
	'''Recorremos la calles a las que se dirige'''
	for j in range(len(streetsTo[i])):
		'''Buscamos el sentido de la calle con mas trafico'''
		if(trafficTo[i][j] > most_traffic):
			'''Guardamos el nombre de la calle y el trafico en dicho tramo'''
			most_traffic = trafficTo[i][j]
			most_traffic_street = streetsTo[i][j].replace('[','').replace(']','').replace('"','')
	print("Calle: " + street)
	print("Sentido con mas trafico: " + most_traffic_street)
	print("Trafico de " + street + "-" + most_traffic_street + ":" + str(most_traffic))
	print("----------------------------------------------------------------------------")
	'''Reiniciamos la variable para comparar los valores del trafico'''	
	most_traffic = 0
