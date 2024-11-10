def main(args):
    print("Programa para restar 2 números")
    n1 = int(input("Escribe un número: "))
    n2 = int(input("Escribe el segundo número: "))
    result = n1 - n2
    print(result)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

