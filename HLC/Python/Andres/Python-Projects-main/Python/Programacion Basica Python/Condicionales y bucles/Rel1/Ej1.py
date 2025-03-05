import sys
def main():
    print("Introduce un numero")
    a=int(input())
    if a>0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")
    return 0
if __name__ == '__main__':
    sys.exit(main())