#Escribe una función que recibe tres textos como parámetros. Uno será el texto a analizar, otro el
#texto a buscar y el tercero el texto que reemplazará al segundo. La función devolverá el texto
#modificado.

import re

def reemplazar_texto(texto_analizar, texto_buscar, texto_reemplazar):
    texto_modificado = re.sub(texto_buscar, texto_reemplazar, texto_analizar)
    return texto_modificado

def main():
    texto_original = input("Escribe un texto: ")
    texto_buscar = input("Escribe un texto para buscar: ")
    texto_reemplazar = input("Escribe el nuevo texto: ")

    texto_modificado = reemplazar_texto(texto_original, texto_buscar, texto_reemplazar)

    print("Texto original:")
    print(texto_original)

    print("Texto modificado:")
    print(texto_modificado)

if __name__ == "__main__":
    main()
