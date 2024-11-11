#Diseña una función python que recibe como parámetro un texto y devuelve una lista con los
#números de teléfono que se han encontrado en dicho texto. Los números tendrán la forma nnn-nnn-
#nnn o nnnnnnnnn o nnn.nnn.nnn. Intenta diseñar tú el patrón, este es sencillo y te vendrá bien
#practicar.
import re

def extraer_telefono(texto):
    # Patrón para números de teléfono en formato nnn-nnn-nnn, nnnnnnnnn o nnn.nnn.nnn
    patron = re.compile(r'\b(?:\d{3}[-.\s]?){2}\d{3}\b|\b\d{9}\b')

    # Buscar coincidencias en el texto
    numeros_telefono = patron.findall(texto)

    return numeros_telefono

# Ejemplo de uso
texto = input("Escribe un texto para comprobar los numeros: ")
telefono_encontrados = extraer_telefono(texto)

print("Números de teléfono encontrados:", telefono_encontrados)


