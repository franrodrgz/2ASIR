import sys
def main():
    print("Elige que operacion quieres realizar")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion")
    c=int(input())
    print("Introduce un numero")
    a=int(input())
    print("Introduce otro un numero")
    b=int(input())
    if c==1:
        print('La suma es')
        print(a+b)
    elif c==2:
        print('La resta es')
        print(a-b)
    elif c==3:
        print('La multiplicacion es')
        print(a*b)
    else:
        print("Operacion no reconocida")
    return 0
if __name__ == '__main__':
    sys.exit(main())