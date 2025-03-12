#!/usr/bin/env python3

import sys
import re
import argparse
import os, shutil

# Pasar un fichero por argumento que lea el contenido y si una linea no cumple con los requisitos la salta, 
# si cumple con los requisitos la añade a un diccionario que contiene los usuarios y una lista con las asignaturas y con todo eso crea un fichero con los que lo cumplen.

def leerFichero(fichero):
	lista = list()
	
	try:
		f = open(fichero)
	except FileNotFoundError:
		print("No existe")
	
	lines = f.readlines()
	
	for line in lines:
		lista.append(line)
	return lista
	
def filtrarContenido(lista):
	fichero = input("Introduce el nombre del fichero donde quieras insertar los usuarios validos: ")
	ruta = input("Inserta una ruta valida para crear la carpeta donde insertaras el archivo de los usuarios(no introduzcas la nueva carpeta): ")
	carpetaNueva = input("Introduce el nombre de la nueva carpeta: ")
	os.chdir(ruta)
	os.mkdir(carpetaNueva)
	dicc = {}
	lista2 = list()
	try:
		f = open(fichero, "w")
	except FileNotFoundError:
		print("Archivo no encontrado")
	for linea in lista:
		a = linea.split(" ")
		usuario = a[2]
		ip = a[5]
		correo = a[8]
		dominio = a[11]
		dni = a[15]+a[18]
		if filtrarIP(ip):
			if filtrarCorreo(correo):
				if filtrarDominio(dominio):
					if filtrarDni(dni):
						print("El usuario "+usuario+" se introducido correctamente")
						for i in range(23,len(a),2):
							b = a[i]
							c = i+1
							lista3 = [a[i],a[c]]
							lista2.append(lista3)
							diccionario={"usuario":usuario,"ip":ip,"correo":correo,"dominio":dominio,"dni":dni,"asignaturas":lista2}
						lista2.sort()
						dicc = str(diccionario)
						x = str(lista2[1][1])
						y = x.strip(",")
						w = str(lista2[0][1])
						z = w.strip(",")
						f.write("Usuario: "+diccionario["usuario"]+"\n"+"IP: "+diccionario["ip"]+"\n"+"Direccion de Correo: "+diccionario["correo"]+"\n"+"Dominio: "+diccionario["dominio"]+"\n"+"DNI: "+diccionario["dni"]+"\n"+"Asignaturas:"+"\n"+"            "+str(lista2[0][0]+" ")+str(z)+"            "+str(lista2[1][0]+" ")+str(y)+"\n")
						lista2 = list()
				else:
					print("El dominio del usuario "+usuario+" no es valido")
			else:
				print("El correo del usuario "+usuario+" es incorrecto")
		else:
			print("La IP del usuario "+usuario+" es incorrecta")
	path = ruta+fichero
	move = ruta+carpetaNueva
	print(move)
	moveto = move
	shutil.move(path,moveto)

	return ip

def filtrarIP(ip):
	
	patron = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
	return re.match(patron, ip)
	
def filtrarCorreo(correo):
	
	patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'
	return re.match(patron, correo)

def filtrarDominio(dominio):
	
	patron = r'^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
	return re.match(patron, dominio)

def filtrarDni(dni):
	
	patron = r'^\d{8}[A-Za-z]$'
	return re.match(patron, dni)

def main():
	## Definición de los parámetros de script (fichero origen obligatorio, fichero salida opcional)
    ## Si no se proporciona fichero de salida, se guardará en "informe.txt" en la misma carpeta
    ## que esté el script
	parser = argparse.ArgumentParser(description="Informe accesos denegados")
	parser.add_argument("origen",help="Es necesario insertar un fichero",nargs=1)
	#parser.add_argument("salida",help="No tienes por que insertarlo",nargs="*")
    
	args = parser.parse_args()
	fichero=leerFichero(args.origen[0])
	filtrarContenido(fichero)

	return 0


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción por el usuario.")
        sys.exit(1)
