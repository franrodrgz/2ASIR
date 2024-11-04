#!/usr/bin/env python

def main(args):
	total=int(input("De cuantos números va a ser la media...?"))
	contador=0
	while contador<total:
		numero=int(input("Introduce un número: "))
		suma=suma+numero
		contador=contador+1
		
		media=suma/total
		return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
