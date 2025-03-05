def extraerIp(linea):
    lista = linea.split(" ")
    return lista[2]
def main(args):
    linea = "eth0: inet 192.168.1.50 netmask 255.255.255.0 broadcast 192.168.1.255"
    ip=extraerIp(linea)
    print(ip)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
