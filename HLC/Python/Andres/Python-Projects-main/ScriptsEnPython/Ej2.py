#!/usr/bin/python3
import sys
import re
import argparse
def lectura(texto):
    f=open(texto[0],'r')
    a=f.read()
    f.close()
    return a
def check(fecha):
    patron = r'([0-2][0-9]|3[0-1])([\/|-])([0-9]|1[0-2])([\/|-])(\d{2})'
    fechas = re.finditer(patron,fecha)
    for match in fechas:
        print(match.group())
def main(args):
    return 0
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fichero",help="Nombre del fichero", nargs=1)
    args = parser.parse_args()
    check(lectura(args.fichero))
    sys.exit(main(sys.argv))
