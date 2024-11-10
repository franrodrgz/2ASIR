def main(args):
	control=1
	suma=0
	while control<=10:
		suma=suma+control
		control=control+1
	print(suma)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
