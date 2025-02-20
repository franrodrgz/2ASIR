#!/usr/bin/env python

def main(args):
	micadena=input("Introduce una cadena de caracteres: ")
	print("HECHO USANDO RANGE")
	for i in range(len(micadena)):
		print(micadena[i])
	print("HECHO USANDO LA CARACTERÍSTICA ITERABLE DE LAS CADENAS")
	for micadena in micadena:
		print(micadena)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
