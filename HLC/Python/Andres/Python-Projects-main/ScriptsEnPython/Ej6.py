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
    patron = r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
    coincidencias= re.findall(patron, texto)
    print(coincidencias)
    for match in coincidencias:
        print(match)
def main(args):
    return 0
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fichero",help="Nombre del fichero", nargs=1)
    args = parser.parse_args()
    print(args)
    check(lectura(args.fichero[0]))
    sys.exit(main(sys.argv))