def main(args):
    print("Introduce un numero para saber si es par o impar")
    n = int(input())
    resto= n % 2
    if resto==0:
        print("Es par")
    else:
        print("Es impar")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
