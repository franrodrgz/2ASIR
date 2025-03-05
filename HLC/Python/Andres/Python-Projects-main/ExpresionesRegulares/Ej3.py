#!/usr/bin/env python
import sys
import re
def correocheck(x):
    patron = r'\b\d{3}[.]\d{3}[.]\d{3}|\b\d{3}\d{3}\d{3}|\b\d{3}[-]\d{3}[-]\d{3}'
    return bool(re.findall(patron, x))

def main(args):
    patron = sys.argv[1]
    if correocheck(patron):
        print ("Patron correto")
    else:
        print ("Patron incorrecto")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))