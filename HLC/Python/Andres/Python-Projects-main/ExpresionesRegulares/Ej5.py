#!/usr/bin/env python
import sys
import re
import os
def lectura(texto):
    f=open(texto,'r')
    a=f.read()
    f.close()
    return a
def checker(texto):
    patron = r'<(\w+)*>'
    coincidencias= re.findall(patron , texto)
    print(coincidencias)

def main(args):
    print(os.listdir())  # Muestra los archivos en la carpeta actual
    texto = sys.argv[1]
    print (lectura(texto))
    a=lectura(texto)
    checker(a)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))