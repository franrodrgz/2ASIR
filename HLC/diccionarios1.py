#!/usr/bin/env python
def introducirDatos():
    datitos={}
    nservidores=int(input("Cuantos servidores quieres introducir: "))
    for i in range(nservidores):
        ip=input("Introduce un adirección IP valida: ")
        masc=input("Introduce la máscara de red: ")
        gateway=input("Introduce la puerta de enlace de la red: ")
        DNS=input("Introduce los servidores DNS: ")
        datitos.update({ip,masc,gateway,DNS})
    print({datitos})

def mostrarDatos(diccionario):
    # Mostrar las claves del diccionario.
    for servidor in diccionario:
        print(servidor)
    # Mostrar un recorrido de los valores de cada clave.
    for servidor in diccionario:
        print(f"{servidor}--->{diccionario[servidor]}")
    # Mostrar cada clave con sus datos introducidos en el segundo diccionario.
    for servidor in diccionario:
        print(f"{servidor}")
        for dato in diccionario[servidor]:
            print(f"\t{dato}--->{diccionario[servidor][dato]}")
    # Esta es otra manera de hacer lo anterior.
    for servidor in diccionario:
        print(f"{servidor}")
        for clave,valor in diccionario[servidor].items():
            print(f"\t{clave}--->{valor}")
    # Aqui indica que si la clave es DNS que muestre los valores indicados de esa lista.
    for servidor in diccionario:
        print(f"{servidor}")
        for clave,valor in diccionario[servidor].items():
            if clave=="DNS":
                print(valor[0],valor[1])
    # Prueba 1
    for servidor in diccionario:
        print(f"{servidor}")
        for clave,valor in diccionario[servidor].items():
            if clave=="DNS":
                print("\t"+"DNS--->"+valor[0],valor[1])
            else:
                print(f"\t{clave}--->{valor}")
    # Prueba 2
    for servidor in diccionario:
        print(f"{servidor}")
        for clave,valor in diccionario[servidor].items():
            if clave=="DNS":
                print("\t"+"DNS:")
                for i in valor:
                    print("\t\t"+i)
            else:
                print(f"\t{clave}--->{valor}")

def main(args):
    datos={
          'Serv1':{
                  "ip":"192.168.8.1",
                  "masc":"255.255.255.0",
                  "gateway":"192.168.8.1",
                  "DNS":["1.1.1.1","8.8.8.8"]
                  },
          'Serv2':{
                  "ip":"192.168.8.2",
                  "masc":"255.255.255.0",
                  "gateway":"192.168.8.1",
                  "DNS":["1.1.1.1","8.8.8.8"]
                  }
          }
    introducirDatos()
    mostrarDatos(datos)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
