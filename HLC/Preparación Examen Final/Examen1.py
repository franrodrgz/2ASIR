#!/usr/bin/env python

def main(args):
	print("¡Bienvenido al juego de adivinanzas de números!")
	print("Estoy pensando en un número entre 1 y 100")
	import random

	numeroSecreto = random.randint(1,100)
	
	a = 0
	i = 0
	
	while a!=numeroSecreto:
		a = int(input("Cual es tu numero elegido: "))
		if a>numeroSecreto:
			print("Tu numero escogido es mas pequeño.")
			i+=1
		elif a<numeroSecreto:
			print("Tu numero escogido es mas grande.")
			i+=1
		else:
			i+=1
			print("Enhorabuena! Has terminado la adivinanza en "+str(i)+" intentos.")
			
	print("El numero era el "+str(numeroSecreto))
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
