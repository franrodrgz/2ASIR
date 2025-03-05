#!/usr/bin/env python
import sys
import re
def fechacheck(fecha):
    patron = r'^([0-2][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{2}$'
    return bool(re.match(patron,fecha))
def main(args):
    fecha = sys.argv[1]
    if fechacheck(fecha):
        print ("Fecha correto")
    else:
        print ("Fecha incorrecto")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))