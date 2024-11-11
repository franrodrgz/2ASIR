def main(args):
    numero = int(input("Introduce un numero para ver su factorial: "))

    if numero <= 0:
        print("El numero debe ser mayor que 0")
    else:
        factorial = 1
        control = 1

        while control <= numero:
            factorial *= control
            control += 1

        print("El factorial de ", numero, " es ", factorial)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))