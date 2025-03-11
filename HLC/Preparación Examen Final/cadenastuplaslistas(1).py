#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Función para pasar de cadenas a tuplas
def CreaTuplas(registros):

	lista = list()
	for i in registros:
		lista2 = i.split(" - ")
		tupla = (lista2[0],lista2[1],lista2[2],lista2[3])
		lista.append(tupla)
	return lista
	

# Función para filtrar intentos fallidos
def CuentaFallidos(RegistrosEnTuplas):
	fallidos = list()
	for i in range(len(RegistrosEnTuplas)):
		if RegistrosEnTuplas[i][3]=="fallido":
			fallidos.append(RegistrosEnTuplas[i])
	return fallidos

# Función principal. NO PUEDES CAMBIAR NADA DE LA FUNCIÓN PRINCIPAL
def main(args):
    # Datos a tratar
    registros = [
        "u123 - 192.168.1.10 - 2024-11-13 08:30 - exitoso",
        "u456 - 192.168.1.11 - 2024-11-13 09:00 - fallido",
        "u123 - 192.168.1.10 - 2024-11-13 09:10 - fallido",
        "u789 - 192.168.1.12 - 2024-11-13 09:15 - exitoso",
        "u456 - 192.168.1.11 - 2024-11-13 09:30 - exitoso",
        "u123 - 192.168.1.10 - 2024-11-13 10:00 - fallido"
]

    # Uso de las funciones
    RegistrosEnTuplas = CreaTuplas(registros)
    print("Registros procesados:", RegistrosEnTuplas)

    IntentosFallidos = CuentaFallidos(RegistrosEnTuplas)
    print("Intentos fallidos:", IntentosFallidos)


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
