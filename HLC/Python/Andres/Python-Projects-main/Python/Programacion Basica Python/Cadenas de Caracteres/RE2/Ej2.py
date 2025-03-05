def verificaip(ip):
    lista = ip.split(".")
    if lista[0] == "192" and lista[1] == "168" and lista[2] == "1" and 1 < int(lista[3]) < 255:
        print(lista)
        return "La ip es correcta"
    return "La ip no es correcta"
def main(args):
    ip=input("Introduce la ip: ")
    print(verificaip(ip))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
