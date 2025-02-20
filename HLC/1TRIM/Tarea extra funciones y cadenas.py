#!/usr/bin/env python

def domain(dominio):
	for i in range(len(usuario)):
		for o in range(len(usuario[i])):
			if usuario[i][o] == "@":
				return (domain[i])
					
def email(correo):
	for i in range(len(correo[i])):
		if correo[i] == "@":

def main(args):
	usuario = ("Fran","PC03","192.168.8.13","romufr_aliesma20@iesmedinaazahara.es")
	correo = email(usuario)
	dominio = domain(email)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
