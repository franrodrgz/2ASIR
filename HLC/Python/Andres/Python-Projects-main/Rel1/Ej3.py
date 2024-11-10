#!/usr/bin/env python
def main(args):
    num1=input("Introduce el primer numero ")
    num2=input("Introduce el segundo numero ")
    sum=int(num1)-int(num2)
    print(sum)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))