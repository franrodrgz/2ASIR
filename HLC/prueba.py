def main(args):
    tupla=("@2asir.net","192.168.1.1")
    lista=list()

    for i in range(10,30):
        lista.append("usuario"+str(i)+tupla[0])
        lista.append("192.168.1."+str(i))
    print(lista)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))