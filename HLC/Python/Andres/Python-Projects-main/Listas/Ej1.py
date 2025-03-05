#Crear una lista de 5 asignaturas y mostrarlas alfabeticamente
def main(args):
    lista=['Filosofia','Fisica','Mates','Latin','Historia']
    lista.sort(reverse=False)
    print (lista)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))