# Diseña una función python que recibe como parámetro un texto y devuelve un entero que indica
# cuantas fechas se han encontrado en dicho texto. Las fechas tendrán la forma dd-mm-aaaa o
# dd/mm/aaaa. Intenta diseñar tú el patrón, este es sencillo y te vendrá bien practicar.

import re

def contar_fechas(texto):
    # Patrón para encontrar fechas con el formato dd-mm-aaaa o dd/mm/aaaa
    patron_fecha = re.compile(r'\b\d{2}[-/]\d{2}[-/]\d{4}\b')

    # Buscar fechas en el texto
    fechas = patron_fecha.findall(texto)

    # Devolver la cantidad de fechas encontradas
    return len(fechas)

# Funcionamiento de la funcion

texto_ejemplo = input("Introduce un texto: ")
cantidad_fechas = contar_fechas(texto_ejemplo)

print(f"Se encontraron {cantidad_fechas} fechas en el texto.")
