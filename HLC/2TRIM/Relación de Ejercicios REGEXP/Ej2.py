#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#EJERCICIO 2
#Diseña una función python que recibe como parámetro un texto y devuelve un entero que indica
#cuantas fechas se han encontrado en dicho texto. Las fechas tendrán la forma dd-mm-aaaa o
#dd/mm/aaaa. Intenta diseñar tú el patrón, este es sencillo y te vendrá bien practicar.

import re

def main(args):
    texto = "20/12/2025"
    
    patron = r"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}"
    
    # Buscar todas las fechas en el texto
    fechas = re.finditer(patron, texto)
    
    if fechas:
        for fecha in fechas:
            inicio = fecha.start()
            fin = fecha.end()
            print(f"Fecha encontrada: {fecha.group()}")
    else:
        print("No hay fechas")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

