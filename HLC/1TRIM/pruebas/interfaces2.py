#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################################################################
#          FUNCIÓN: cargaDatos    
#          OBJETIVO: crear una lista con las líneas del fichero
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

def filtrarDatos(lineas):
    dicc = {}  # Crear un diccionario vacío
    i = 0  # Contador para las claves

    for linea in lineas:
        if "gateway" not in linea:  # Filtrar líneas que no contienen "gateway"
            clave = f"eth{i}"  # Crear una clave única
            dicc[clave] = linea.strip()  # Agregar la línea al diccionario
            i += 1  # Incrementar el contador

    return dicc

#################################################################################################
#          FUNCIÓN: mostrarFiltrados   
#          OBJETIVO: mostrar por pantalla el diccionario con los datos ya filtrados
#          PARÁMETROS DE ENTRADA: diccionario con los datos filtrados
#          PARÁMETROS DE SALIDA: ninguno. Muestra por pantalla el contenido
#################################################################################################  

def mostrarFiltrados(dicc):
    for clave, valor in dicc.items():
        print(f"{clave}: {valor}")

#################################################################################################

def main(args):
    if len(args) != 2:
        print("Uso: python script.py <nombre_archivo>")
        return 1

    nombre_archivo = args[1]

    # Uso de las funciones
    listaLineas = cargaDatos(nombre_archivo)
    if not listaLineas:
        return 1  # Salir si no se pudo cargar el archivo

    print("Contenido del archivo:\n")
    mostrarDatos(listaLineas)

    print("\nInterfaces sin gateway:\n")
    datosFiltrados = filtrarDatos(listaLineas)
    mostrarFiltrados(datosFiltrados)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
