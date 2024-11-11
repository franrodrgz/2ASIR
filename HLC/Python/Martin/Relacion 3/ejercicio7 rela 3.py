def main(args):
	numero=int(input("Introduce una tabla que sea del 1 al 10: "))
	control=1
	print("Tabla del ", numero)
	while control<=10:
		print(numero, " x ", control, " = ", numero*control)
		control=control+1
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
