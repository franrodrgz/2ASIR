#!/usr/bin/env python

def main(args):
	num1=int(input("Introduzca el primer número: "))
	num2=int(input("Introduzca el segundo número: "))
	resultado=num1*num2
	print("El resultado es",resultado)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
