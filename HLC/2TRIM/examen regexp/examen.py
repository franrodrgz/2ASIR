#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#################################################################################################
####    Programa que analiza un fichero de log con las conexiones a un servidor y pasa a otro  ##
####    fichero la información de las conexiones fallidas.                                    ###
#################################################################################################
import re
import sys
import argparse

def leer_archivo():
    ## Función que lee el archivo que recibe como parámetro y devuelve una lista con las 
    ## líneas de texto
    

def buscar_errores():
    ## Funcion que recibe una lista con las lineas del fichero y devuelve una lista
    ## con las filas en la que hubo un acceso denegado
    

def guardar_informe(ruta_salida, errores):
    ## Función que recibe la ruta del fichero de salida y la lista de intentos denegados
    ## y guarda en el fichero solamente la fecha y hora de conexión y el usuario que intentó conectar
  
    
    

def main():
    ## Definición de los parámetros de script (fichero origen obligatorio, fichero salida opcional)
    ## Si no se proporciona fichero de salida, se guardará en "informe.txt" en la misma carpeta
    ## que esté el script
    parser = argparse.ArgumentParser(description="Informe accesos denegados")
    parser.add_argument(
    
                       ## borra esto y escribe aquí la definición de tu argumento
                       )
    parser.add_argument(
    
                       ## borra esto y escribe aquí la definición de tu argumento
    
                       )
    
    args = parser.parse_args()
    
    
    
   
    ## Cuerpo principla. Define el patrón y llama a las funciones 
   
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción por el usuario.")
        sys.exit(1)
