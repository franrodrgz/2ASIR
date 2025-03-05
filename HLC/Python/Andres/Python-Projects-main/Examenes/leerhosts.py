#!/usr/bin/python3
import sys
import re
import argparse
def lectura(texto):
    dict = []
    f=open(texto,'r')
    for line in f:
        resultado = check(line)
        if resultado:
            dict.append({"nombre": resultado[1],"ip": resultado[0]})
    f.close()
    for item in dict:
        print(f"Nombre: {item['nombre']}, Ip: {item['ip']}")
def check(texto):
    patron = r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}'
    if bool(re.match(patron, texto)):
        a = texto.strip().split()
        print(a)
        return a
    return None
def escritura(usuario,ip):
    for list1,list2 in zip(usuario,ip):
        with open("hosts","a") as archivo:
            archivo.writelines(f"{list2}  {list1}\n")
def main(args):
    return 0
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fichero",help="Nombre del fichero", nargs=1)
    parser.add_argument("-u",help="nombre del nuevo usuario",nargs="*")
    parser.add_argument("-ip",help="Ip",nargs="*")
    args = parser.parse_args()
    print(args)
    lectura(args.fichero[0])
    escritura(args.u,args.ip)
    sys.exit(main(sys.argv))