#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    try:
        archivo=open("txt.txt")
    except FileNotFoundError:
        print("Archivo no encontrado")

    contenido=archivo.read()
    print("CONTENIDO COMPLETO\n")
    print(contenido)

    archivo.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
