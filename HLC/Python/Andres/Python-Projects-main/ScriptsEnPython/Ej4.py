#!/usr/bin/python3
import sys
import re
import argparse
def lectura(texto):
    f=open(texto,'r')
    a=f.read()
    f.close()
    return a
def check(texto,patron,cambio):
    resultado = re.sub(patron,cambio,texto)
    escritor(resultado)

def escritor(resultado):
    with open("salida.txt","a") as archivo:
        archivo.writelines(resultado)
def main(args):
    return 0
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fichero",help="Nombre del fichero", nargs=1)
    parser.add_argument("patron",help="Texto a reemplazar", nargs=1)
    parser.add_argument("cambio",help="Texto nuevo", nargs=1)
    args = parser.parse_args()
    print(args)
    check(lectura(args.fichero[0]),args.patron[0],args.cambio[0])
    sys.exit(main(sys.argv))
