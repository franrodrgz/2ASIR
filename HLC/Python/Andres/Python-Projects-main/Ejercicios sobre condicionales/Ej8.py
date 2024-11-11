import sys
def main():
    print("Introduce un numero")
    a=int(input())
    print("Introduce otro un numero")
    b=int(input())
    print("Introduce otro un numero")
    c=int(input())
    if a>b and a>c:
        print("El mayor es")
        print(a)
    elif b>a and b>c:
        print("El mayor es")
        print(b)
    else:
        print("El mayor es")
        print(c)
    return 0
if __name__ == '__main__':
    sys.exit(main())