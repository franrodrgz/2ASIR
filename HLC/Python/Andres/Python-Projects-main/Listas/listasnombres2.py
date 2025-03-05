def main(args):
    tupla=("@gmail.com","192.168.100.50")
    lista=list()
    x=tupla[1].split(".")
    y=int(x[3])
    for i in range(0,1):
        nombre=input("Usuario: ")
        apellido=input("Apellido: ")
        apellido2=input("Apellido2:")
        x=nombre.casefold()
        ap1=apellido.casefold()
        ap2=apellido2.casefold()
        c=y
        tupla2=(nombre+", "+apellido+", "+apellido2,ap1[0:2]+ap2[0:2]+x[0:2]+"_iesma"+str(i)+tupla[0],"192.168.100."+str(c))
        lista.append(tupla2)
        y+=1
    print(lista)
    for nombre, usuario, ip in lista:
        usuario.lower()
        print("Nombre completo :",nombre)
        print("Correo: ",usuario," Ip: ",ip)
    return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))