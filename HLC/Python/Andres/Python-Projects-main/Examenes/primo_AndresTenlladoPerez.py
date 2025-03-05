import sys
#AndresTenlladoPerez
def entradaControlada():
	for i in range(0,10):
		a=int(input("Introduce un numero entero positivo: "))
		if a>1:
			return a
	print("Se te han acabado el numero de intentos")
	a=0
	return a

def esPrimo(a):
	for i in range(2,a):
		if a % i == 0:
			c=str(a)+" no es un numero primo."
			return c
	c=str(a)+" es un numero primo."
	return c

def main(args):
	a=entradaControlada()
	if a!=0:
		print(esPrimo(a))
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
