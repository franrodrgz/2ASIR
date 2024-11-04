#!/usr/bin/env python

def main(args):
	print("¡Bienvenido al juego de adivinanzas de números!")
	print("Estoy pensando en un número entre 1 y 100")
	import random
	numero_secreto = random.randint(1,100)
	i=0
	a=0
	while a!=numero_secreto: 
		a=int(input("Introduce tu número"))
		if a>numero_secreto:
			print("El número secreto es menor")
			i+=1
		elif a<numero_secreto:
			print("El número secreto es mayor")
			i+=1
		elif a==numero_secreto:
			print("¡Felicidades! Has adivinado el numero en",+i,"intentos")
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
