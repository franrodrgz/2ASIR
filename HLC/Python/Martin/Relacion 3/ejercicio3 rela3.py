def main(args):
	print("Contador y muestra los numeros")
	numero1=int(input("Introduce el inicio: "))
	numero2=int(input("Introduce el final: "))
	control=numero1
	while control<=numero2:
		print(control)
		control=control+1
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
