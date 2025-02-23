def main(args):
    tupla=("@2asir.net","192.168.1.1")
    lista=list()

    for i in range(10,30):
        tupla2=("usuario"+str(i)+tupla[0],"192.168.1."+str(i))
        lista.append(tupla2)
    for usuario, ip in lista:
        print("Usuario: ",usuario,"IP: ",ip)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))