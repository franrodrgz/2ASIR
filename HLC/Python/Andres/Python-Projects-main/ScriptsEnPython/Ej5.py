#!/usr/bin/python3
import sys
import re
import argparse
def lectura(texto):
    f=open(texto,'r')
    a=f.read()
    f.close()
    return a
def check(texto):
    patron = r'<(\w+)*>'
    coincidencias= re.findall(patron , texto)
    print(coincidencias)
def main(args):
    return 0
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fichero",help="Nombre del fichero", nargs=1)
    args = parser.parse_args()
    print(args)
    if ".xml" in args.fichero[0]:
        print ("El fichero es tiene extension xml")
        texto = lectura(args.fichero[0])
        if '<?xml version="1.0" encoding="UTF-8"?>' in texto:
            print("Contiene la primera linea de los archivos xml")
            check(texto)
    else:
        print("Error el fichero no tiene extension xml")
    sys.exit(main(sys.argv))
