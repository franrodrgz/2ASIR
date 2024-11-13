def main(args):
    tupla=("x@2asir.net","192.168.1.1")
    lista = tupla[0].split("@")
    for i in range(10,30):
        lista[0]="usuario",i
        print(lista)
    lista = tupla[1].split(".")
    for i in range(10,30):
        lista[3]=i
        print(lista)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))