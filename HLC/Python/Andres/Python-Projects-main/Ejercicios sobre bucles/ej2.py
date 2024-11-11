#!/usr/bin/env python
#Diseñar un algoritmo que muestre la suma de los 10 primeros números.
def main(args):
    i = 1
    b = i
    while i < 10:
        i += 1
        b += i
    print(b)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))