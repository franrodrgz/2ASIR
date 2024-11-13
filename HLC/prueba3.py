def main(args):
    tupla=("@iesmedinaazahara.es","192.168.1.")
    lista=list()
    for i in range(0,2):
        nombre=input("Introduce tu nombre: ")
        apellido1=input("Introduce tu primer apellido: ")
        apellido2=input("Introduce tu segundo apellido: ")
        n=(nombre[0:2])
        a1=(apellido1[0:2])
        a2=(apellido2[0:2])
        ap1=a1.casefold()
        ap2=a2.casefold()
        n1=n.casefold()
        tupla2=(nombre+" "+apellido1+" "+apellido2,ap1+ap2+n1+"_iesma2324"+tupla[0],tupla[1]+str(i))
        lista.append(tupla2)
    for nombre, correo, ip in lista:
        print("Nombre Completo: "+nombre,"Correo Electronico: "+correo,"IP: "+ip)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))