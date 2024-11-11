#!/usr/bin/env python
def main(args):
    print("Cuantos numeros quieres introducir")
    n=int(input())
    i=int(0)
    b=int(0)
    while i <n:
        print("Introduce un numero")
        a=int(input())
        b += a
        i += 1
    b=b/n
    print(b)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
