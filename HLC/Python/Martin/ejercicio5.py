#Escribe una función que recibe un texto y devuelve una lista con las etiquetas xml encontradas en
#dicho texto.
#Escribe un programa python que pregunta el nombre de un archivo xml y usa la función anterior
#para mostrar una lista de las etiquetas xml usadas en dicho archivo

#!/usr/bin/python3

import re

def encontrar_etiquetas_xml(texto):
    # Patrón para buscar etiquetas XML
    patron_etiquetas = re.compile(r'<[^>]+>')

    # Buscar coincidencias en el texto
    etiquetas_encontradas = patron_etiquetas.findall(texto)

    return etiquetas_encontradas

def main():
    # Preguntar por el nombre del archivo XML
    nombre_archivo = input("Ingrese el nombre del archivo XML: ")

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Leer el contenido del archivo
            contenido = archivo.read()

            # Encontrar etiquetas XML en el contenido
            etiquetas_encontradas = encontrar_etiquetas_xml(contenido)

            # Mostrar las etiquetas encontradas
            print("Etiquetas XML encontradas:")
            for etiqueta in etiquetas_encontradas:
                print(etiqueta)

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'.")

if __name__ == "__main__":
    main()
