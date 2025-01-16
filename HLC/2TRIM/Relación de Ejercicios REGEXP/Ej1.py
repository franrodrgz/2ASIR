#!/usr/bin/env python
# -*- coding: utf-8 -*-

#EJERCICIO 1
#Diseña una función en python que reciba como parámetro una cadena de texto y devuelva True si es
#un correo electrónico y False si no lo es. No es necesario que diseñes el patrón, puedes encontrarlo
#facilmente en internet.

def main(args):
    import re
    
    email = input("Introduzca una direccion de correo: ")
    patron = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    
    comp = re.compile(patron)
    validar = comp.match(email)
    
    if (validar):
        inicio = validar.start()
        final = validar.end()
        print("El correo es valido")
    else:
        print("El correo no es valido")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
