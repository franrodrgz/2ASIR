#!/usr/bin/env python

def main(args):
	num1=int(input("Introduce el primer número: "))
	num2=int(input("Introduce el segundo número: "))
	num3=int(input("Introduce el tercer número: "))
	num4=int(input("Introduce el cuarto número: "))
	num5=int(input("Introduce el quinto número: "))
	suma=num1+num2+num3+num4+num5
	media=suma/5
	print("La media de estos números es: ",media)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
