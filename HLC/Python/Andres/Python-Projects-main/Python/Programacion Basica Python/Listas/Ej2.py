def main(args):
    lista=list()
    i=0
    for i in range(0,5):
        lista.append(input("Escribe la asignatura"))
    lista.sort(reverse=False)
    print (lista)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))