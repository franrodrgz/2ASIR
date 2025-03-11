#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#################################################################################################
####    Programa que analiza un fichero de log con las conexiones a un servidor y pasa a otro  ##
####    fichero la información de las conexiones fallidas.                                    ###
#################################################################################################
import re
import sys
import argparse

def leer_archivo(ruta):
    ## Función que lee el archivo que recibe como parámetro y devuelve una lista con las 
    ## líneas de texto
	lista = list()
	
	try:
		f = open(ruta)
	except FileNotFoundError:
		print("No existe")
	
	l = f.readlines()
	
	for line in l:
		lista.append(line)
	return lista


def buscar_errores(texto):
    ## Funcion que recibe una lista con las lineas del fichero y devuelve una lista
    ## con las filas en la que hubo un acceso denegado

	lista = list()
	patron = "Access denied"
	for linea in texto:
		ld = re.search(patron, linea)
		if(ld):
			lista.append(linea)
	return lista


def guardar_informe(ruta_salida, errores):
    ## Función que recibe la ruta del fichero de salida y la lista de intentos denegados
    ## y guarda en el fichero solamente la fecha y hora de conexión y el usuario que intentó conectar
    
	with open(ruta_salida, "w") as archivo:
		for linea in errores:
			a = linea.split()
			archivo.writelines(f"{a[0]} {a[2]}\n")
	print(f"{ruta_salida} lista creada con los errores")

def main():
    ## Definición de los parámetros de script (fichero origen obligatorio, fichero salida opcional)
    ## Si no se proporciona fichero de salida, se guardará en "informe.txt" en la misma carpeta
    ## que esté el script
    parser = argparse.ArgumentParser(description="Informe accesos denegados")
    parser.add_argument("origen",help="Fichero origen obligatorio",nargs=1)
    parser.add_argument("salida",help="Fichero salida opcional",nargs="*")
    
    args = parser.parse_args()
    
    
    ## Cuerpo principla. Define el patrón y llama a las funciones
    texto=leer_archivo(args.origen[0])
    if args.salida:
        ruta_salida = args.salida[0]
    else:
        ruta_salida = "salida.txt"
    errores = buscar_errores(texto)
    guardar_informe(ruta_salida,errores)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción por el usuario.")
        sys.exit(1)
