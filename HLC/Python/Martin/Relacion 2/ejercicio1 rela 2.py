def main(args):
    print("Introduce un numero para saber si es positivo o negativo")
    n = int(input())
    if n >= 0:
        print("Es positivo")
    else:
        print("Es negativo")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

