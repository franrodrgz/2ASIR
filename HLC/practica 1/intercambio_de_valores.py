#!/usr/bin/env python

def main(args):
	num1=int(input("Introduce un número: "))
	num2=int(input("Introduce un número: "))
	num3=num2
	num4=num1
	print("Los números son: ",num3,num4)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
