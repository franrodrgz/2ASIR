#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################################################################
#          FUNCIÓN: cargaDatos    
#          OBJETIVO: crear unalista con las líneas del fichero
#          PARÁMETROS DE ENTRADA: una cadena de texto con el nombre del fichero a leer
#          PARÁMETROS DE SALIDA: una lista con las líneas del fichero
#################################################################################################   

def cargaDatos():
	
	nFichero = input("Cual es la ruta del fichero: ")
	
	try:
		fichero = open(nFichero)
	except FileNotFoundError:
		print("No se a encontrado el fichero.")
		
	a = fichero.readlines()
	fichero.close()
	return a


#################################################################################################
#          FUNCIÓN: mostrarDatos    
#          OBJETIVO: mostrar por pantalla la lista de líneas
#          PARÁMETROS DE ENTRADA: lista con las líneas extraídas del fichero
#          PARÁMETROS DE SALIDA: no devuelve nada. Solo muestra por pantalla
#################################################################################################   

def mostrarDatos(listaLineas):
	
	lista = list()
	
	for i in listaLineas:
		lista.append(i)
	print(lista)
	
#################################################################################################
#          FUNCIÓN: filtrarDatos   
#          OBJETIVO: crear un diccionario con las líneas que cumplen una condición.
#          PARÁMETROS DE ENTRADA: lista con las líneas extraídas del fichero
#          PARÁMETROS DE SALIDA: diccionario con las líneas del fichero que contienen "gateway". 
#                                La clave será el número de puerto y el protocolo y los datos el
#                                resto de la línea.
#################################################################################################   

def filtrarDatos(listalineas):
	diccionario = {}
	nombre = list()
	for linea in listalineas:
		linea = linea.split(" ")
		if "gateway" not in linea:
			diccionario[linea[1]]=[linea[2],linea[3],linea[4],linea[5],linea[6],linea[7]]
	return diccionario
    
#################################################################################################
#          FUNCIÓN: mostrarFiltrados   
#          OBJETIVO: mostrar por pantalla el diccionario con los datos ya filtrados
#          PARÁMETROS DE ENTRADA: diccionario con los datos filtrados
#          PARÁMETROS DE SALIDA: ninguno. Muestra por pantalla el contenido
#################################################################################################  

def mostrarFiltrados(datosfiltrados):
	for values in datosfiltrados:
		print(values)
		for i in range(len(datosfiltrados[values])):
			print("      ",datosfiltrados[values][i])

#######################################################################################33##########

def main(args):
    # Uso de las funciones
    listaLineas = cargaDatos()
    print("Contenido /etc/networks/interfaces:\n")
    mostrarDatos(listaLineas)
    print("\nInterfaces sin gateway\n")
    datosFiltrados=filtrarDatos(listaLineas)
    mostrarFiltrados(datosFiltrados)
    

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
