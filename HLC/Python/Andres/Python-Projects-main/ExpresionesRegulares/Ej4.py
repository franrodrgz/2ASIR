#!/usr/bin/env python
import sys
import re
def checker(texto, patron, cambio):
    textomod= re.sub(patron , cambio, texto)
    print (textomod)
    return textomod

def main(args):
    texto = sys.argv[1]
    patron = sys.argv[2]
    cambio = sys.argv[3]
    checker(texto,patron,cambio)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))