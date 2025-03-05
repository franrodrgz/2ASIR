#!/usr/bin/python3
import sys
import re
import argparse
def lectura(texto):
    f=open(texto[0],'r')
    a=f.read()
    f.close()
    return a
def check(texto):
    patron = r'\d{3}[.]\d{3}[.]\d{3}|\d{3}\d{3}\d{3}|\d{3}[-]\d{3}[-]\d{3}'
    resultado = re.finditer(patron,texto)
    escritor(resultado)

def escritor(resultado):
    for match in resultado:
        with open("salida.txt","a") as archivo:
            archivo.writelines(f'{match.group()} \n')
def main(args):
    return 0
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fichero",help="Nombre del fichero", nargs=1)
    args = parser.parse_args()
    check(lectura(args.fichero))
    sys.exit(main(sys.argv))
