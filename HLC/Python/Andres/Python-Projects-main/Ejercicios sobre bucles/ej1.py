#!/usr/bin/env python
#Diseñar un algoritmo que muestre los 10 primeros números.
def main(args):
    i=1
    while i <= 10:
        print(i)
        i += 1
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))