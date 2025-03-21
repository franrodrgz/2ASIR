#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    import re
    
    patron = 'tómbola'
    texto = 'La vida es una Tómbola'
    
    comp = re.compile(patron,re.I)
    coincidencia = comp.search(texto)

    if (coincidencia):
        inicio = coincidencia.start()
        fin = coincidencia.end()
        print('Se ha encontrado "{}" en "{}" desde {} hasta {} ({})'.format(patron, texto, inicio, fin, texto[inicio:fin]))
    else:
        print("El patron indicado no se encuentra en el texto")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
