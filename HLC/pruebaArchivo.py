#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    lista=["hola\n","adios\n"]
    try:
        f = open("archivo.txt","a")
        f.writelines(lista)
    except FileNotFoundError:
        print("No ta creao")

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
