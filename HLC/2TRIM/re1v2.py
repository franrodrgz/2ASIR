#!/usr/bin/env python
import re

# SEARCH busca la primera ubicación donde el patrón pattern de la expresión regular produce una coincidencia
def buscar():
	texto = input("Introduce el texto a examinar: ")
	patron = input("Introduce el patron: ")

	s=re.search(patron, texto)
	
	if (s):
		inicio = s.start()
		fin = s.end()
		print("si")
	else:
		print("no no no")

# MATCH si cero o más caracteres al principio de la cadena string coinciden con el patrón pattern de la expresión regular, retorna un objeto Match correspondiente.
def buscar2():
	texto = input("Introduce el texto a examinar: ")
	patron = input("Introduce el patron: ")

	s=re.match(patron, texto)
	
	if (s):
		inicio = s.start()
		fin = s.end()
		print("si")
	else:
		print("no no no")

# SPLIT
def buscar3():
	patron=r'\W+'
	texto = input("Introduce el texto a examinar: ")
	s=re.split(patron,texto)
	if (s):
		print(s)
		print(f"Hay {len(s)} palabras")
	else:
		print("El patrón no está en el texto")

#  SUB Remplaza cadenas
def buscar4():
	texto = input("Introduce el texto a examinar: ")
	patron = input("Introduce lo que quieres modificar: ")
	mod = input("Introduce la nueva cadena: ")
	
	flag=re.I
	modificar = re.sub(patron,mod,texto,0,flag)
	print(modificar)

#  SUBN Remplaza cadenas y devuelve una tupla
def buscar5():
	texto = input("Introduce el texto a examinar: ")
	patron = input("Introduce lo que quieres modificar: ")
	mod = input("Introduce la nueva cadena: ")
	
	flag=re.I
	modificar = re.subn(patron,mod,texto,0,flag)
	print(f"El nuevo texto es:\n {modificar[0]} \n y se han hecho {modificar[1]} cambios")

def main(args):
	buscar()
	buscar2()
	buscar3()
	buscar4()
	buscar5()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
