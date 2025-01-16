#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#EJERCICIO 3
#Diseña una función python que recibe como parámetro un texto y devuelve una lista con los
#números de teléfono que se han encontrado en dicho texto. Los números tendrán la forma nnn-nnn-
#nnn o nnnnnnnnn o nnn.nnn.nnn. Intenta diseñar tú el patrón, este es sencillo y te vendrá bien
#practicar.

import re

def main(args):
    
    patron = r'([0-9]{3}-[0-9]{3}-[0-9]{3})|([0-9]{3}\.[0-9]{3}\.[0-9]{3})|([0-9]{9})'
    
    telefono = input("Introduce un número de teléfono: ")
    
    comp = re.compile(patron)
    validar = comp.match(telefono)
    
    if (validar):
        inicio = validar.start()
        fin = validar.end()
        print("El número de teléfono es valido")
    else:
        print("No es un número de teléfono valido")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
