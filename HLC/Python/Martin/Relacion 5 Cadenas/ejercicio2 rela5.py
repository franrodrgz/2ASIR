def main(args):
    cadena = input("Introduce una cadena de caracteres: ")
    espacios=0
    for letras in range (len(cadena)):
		if cadena[letras]==" ":
			espacios+=1
        print(letras)
    return 0
	print(espacios)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
