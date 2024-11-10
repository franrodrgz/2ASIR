def main(args):
    print("Programa para calcular la media de 5 numeros")
    n1 = int(input("Escribe un número: "))
    n2 = int(input("Escribe el segundo número: "))
    n3 = int(input("Escribe el tercer número: "))
    n4 = int(input("Escribe el cuarto número: "))
    n5 = int(input("Escribe el quinto número: "))
    suma = n1 + n2 + n3 + n4 + n5
    media = suma / 5
    print("La media es", media)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
