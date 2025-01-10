#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    import re

    patron = r'\W+'
    texto = 'Esto es un texto de siete palabras'
    
    palabras = re.split(patron,texto)
    
    if (palabras):
        print(palabras)
        print(f"Hay un total de [len(palabras)] palabros")
    else:
        print("Error")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
