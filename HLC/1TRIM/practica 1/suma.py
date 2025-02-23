#!/usr/bin/env python

def main(args):

    num1=int(input("Introduce el primer número: "))
    num2=int(input("Introduce el segundo número: "))
    resultado=num1+num2
    print(resultado)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
