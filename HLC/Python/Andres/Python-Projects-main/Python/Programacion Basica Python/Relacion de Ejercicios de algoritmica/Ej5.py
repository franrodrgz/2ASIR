#!/usr/bin/env python
#solo funciona en python
def main(args):
    num1=input("Introduce el primer numero ")
    num2=input("Introduce el segundo numero ")
    num1,num2=num2,num1
    print(num1,num2)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))