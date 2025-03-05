#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################################################################
#          FUNCIÓN: cargaDatos    
#          OBJETIVO: crear unalista con las líneas del fichero
#          PARÁMETROS DE ENTRADA: una cadena de texto con el nombre del fichero a leer
#          PARÁMETROS DE SALIDA: una lista con las líneas del fichero
#################################################################################################   

def cargaDatos():
	try:
		archivo=open("interfaces.txt")
	except FileNotFoundError:
		print("No se ha podido abrir el archivo")

	lista=archivo.readlines()
	archivo.close()

	return(lista)

#################################################################################################
#          FUNCIÓN: mostrarDatos    
#          OBJETIVO: mostrar por pantalla la lista de líneas
#          PARÁMETROS DE ENTRADA: lista con las líneas extraídas del fichero
#          PARÁMETROS DE SALIDA: no devuelve nada. Solo muestra por pantalla
#################################################################################################   

def mostrarDatos():
	lineas=cargaDatos()
	lista=list()
	for linea in lineas:
		lista.append(linea)
	print(lista)

#################################################################################################
#          FUNCIÓN: filtrarDatos   
#          OBJETIVO: crear un diccionario con las líneas que cumplen una condición.
#          PARÁMETROS DE ENTRADA: lista con las líneas extraídas del fichero
#          PARÁMETROS DE SALIDA: diccionario con las líneas del fichero que contienen "gateway". 
#                                La clave será el número de puerto y el protocolo y los datos el
#                                resto de la línea.
#################################################################################################   

def filtrarDatos():
	lineas=cargaDatos()
	i = 0
	for linea in lineas:
		if "gateway" not in linea:
			clave = f"eth{i}"
			dicc={clave:(linea)}
			i+1
	return dicc

#################################################################################################
#          FUNCIÓN: mostrarFiltrados   
#          OBJETIVO: mostrar por pantalla el diccionario con los datos ya filtrados
#          PARÁMETROS DE ENTRADA: diccionario con los datos filtrados
#          PARÁMETROS DE SALIDA: ninguno. Muestra por pantalla el contenido
#################################################################################################  

def mostrarFiltrados():
	lineas=filtrarDatos()
	print(lineas)

#################################################################################################

def main(args):

	mostrarDatos()
	mostrarFiltrados()
	#Uso de las funciones
	#listaLineas = cargaDatos("interfaces.txt")
	#print("Contenido /etc/networks/interfaces:\n")
	#mostrarDatos(listaLineas)

	#print("\nInterfaces sin gateway\n")
	#datosFiltrados=filtrarDatos(listaLineas)
	#mostrarFiltrados(datosFiltrados)

	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
