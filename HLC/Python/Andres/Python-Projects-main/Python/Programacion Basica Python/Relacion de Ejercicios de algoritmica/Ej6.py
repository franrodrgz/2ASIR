#!/usr/bin/env python
def main(args):
    print("Vamos a calcular la media de 5 numeros")
    num1=input("Introduce el primer numero ")
    num2=input("Introduce el segundo numero ")
    num3=input("Introduce el tercero numero ")
    num4=input("Introduce el cuarto numero ")
    num5=input("Introduce el quinto numero ")
    num1=(float(num1)+float(num2)+float(num3)+float(num4)+float(num5))/5
    print(num1)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))