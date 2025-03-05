import sys
def main():
    print("Introduce un numero")
    a=int(input())
    print("Introduce otro un numero")
    b=int(input())
    if a<0 or b<0:
        print('La suma es')
        print(a+b)
    else:
        print("Tienen que ser los dos negativos")
    return 0
if __name__ == '__main__':
    sys.exit(main())