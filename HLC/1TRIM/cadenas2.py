#!/usr/bin/env python

def main(args):
	mifrase=input("Introduzca una cadena de caracteres: ")
	stop=len(mifrase)
	for mifrase in mifrase:
		print(mifrase[:stop:-1])
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
