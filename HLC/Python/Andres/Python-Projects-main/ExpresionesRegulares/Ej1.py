#!/usr/bin/python3
import sys
import re
def correocheck(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron,correo))
def main(args):
    correo = sys.argv[1]
    if correocheck(correo):
        print ("Correo correto")
    else:
        print ("Correo incorecto")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))