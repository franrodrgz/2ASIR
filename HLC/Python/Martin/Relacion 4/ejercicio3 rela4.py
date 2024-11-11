def main(args):
	numero1=int(input("Introduce el inicio: "))
	numero2=int(input("Introduce el final: "))
	for numeros in range(numero1,numero2,1):
		print(numeros)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

