def main(args):
    print("Introduce dos numeros para saber si son iguales o no")
    n1 = int(input())
    n2 = int(input())
    if n1 == n2:
        print("Son iguales")
    else:
        print("No son iguales")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
