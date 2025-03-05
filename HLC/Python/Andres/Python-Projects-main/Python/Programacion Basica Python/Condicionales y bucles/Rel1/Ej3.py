import sys
def main():
    print("Introduce un numero")
    a=int(input())
    print("Introduce otro un numero")
    b=int(input())
    if a==b:
        print("Los numeros son iguales")
    else:
        print("Los numeros son distintos")
    return 0
if __name__ == '__main__':
    sys.exit(main())