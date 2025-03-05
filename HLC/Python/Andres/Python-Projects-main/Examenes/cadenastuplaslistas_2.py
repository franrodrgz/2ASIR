#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Solución del ejercicio
#AndresTenlladoPerez
# Función para pasar lista de tuplas a lista de cadenas
def Crealineas(registros):
	lista=list()
	for i in range(0,len(registros)):
		cadena=registros[i][0]+"\n "+registros[i][1]+"\n "+registros[i][2]+"\n "+registros[i][3]+"\n "+registros[i][4]
		lista.append(cadena)
	return lista

def main(args):
    # Datos a tratar
    registros = [
                    ("iface eth0", "inet static", "address 192.168.1.1", "netmask 255.255.255.0", "gateway 192.168.1.254"),
                    ("iface eth1", "inet static", "address 192.168.1.2", "netmask 255.255.255.0", "gateway 192.168.1.254")
                ]

    # Uso de las funciones
    lineas = Crealineas(registros)
    print("Contenido /etc/networks/interfaces:\n")
    for linea in lineas:
        print(linea)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
