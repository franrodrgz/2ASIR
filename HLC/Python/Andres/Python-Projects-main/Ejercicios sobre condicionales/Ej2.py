import sys
def main():
    print("Introduce un numero")
    a=int(input())
    if a%2==0:
        print("El numero es par")
    else:
        print("El numero es impar")
    return 0
if __name__ == '__main__':
    sys.exit(main())