#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#AndresTenlladoPerez

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
    with open(ruta, "r") as archivo:
        resultado = archivo.readlines()
    print("Fichero leido")
    return resultado


def buscar_errores(texto):
    ## Funcion que recibe una lista con las lineas del fichero y devuelve una lista
    ## con las filas en la que hubo un acceso denegado
    patron = r'Access denied'
    resultado = []
    for item in texto:
        if bool(re.search(patron,item)):
            resultado.append(item)
    print("Errores encontrados")
    return resultado

def guardar_informe(ruta_salida, errores):
    ## Función que recibe la ruta del fichero de salida y la lista de intentos denegados
    ## y guarda en el fichero solamente la fecha y hora de conexión y el usuario que intentó conectar
	with open(ruta_salida, "w") as archivo:
		for item in errores:
			a = item.split()
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
