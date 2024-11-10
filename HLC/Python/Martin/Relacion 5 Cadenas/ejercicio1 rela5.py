def main(args):
    cadena = input("Introduce una cadena de caracteres: ")
    for letras in range(len(cadena)):
        print(cadena[letras])
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

