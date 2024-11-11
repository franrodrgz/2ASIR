def main(args):
	numero1=int(input("Introduce el inicio: "))
	numero2=int(input("Introduce el final: "))
	control=numero1
	suma=0
	while control<=numero2:
		suma=suma+control
		control=control+1
	print(suma)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
