def main(args):
    control = 1
    suma = 0
    print("Haz la media de 10 números")
    while control <= 10:
        numero = int(input("Introduce un número: "))
        suma = suma + numero
        control = control + 1
    print(suma / 10)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

