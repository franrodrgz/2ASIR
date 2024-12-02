#!/usr/bin/env python

def main(args):
    diccionario={}
    nservers=int(input("Cuantos servidores quieres introducir: "))
    for i in range(nservers):
        nombre=input("Introduce el nombre del servidor: ")
        servicios=int(input("Introduce el numero de servicios: "))
        for i in range(servicios):
            nservicios=input("Introduce el nombre del servicio: ")
            datos=int(input("Introduce el numero de valores del servicio: "))
            for i in range(datos):
                ndatos=input(f"Introduce el valor {i+1} del servicio {nservicios} : ")
    diccionario.update({nombre:{nservicios,ndatos}})
    return diccionario
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
