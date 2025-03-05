import sys
def leer():
    try:
        a=open("Ej2.txt")
    except FileNotFoundError:
        print("Archivo no encontrado")
    lista = list()
    nombre = list()
    lista2=list()
    lista3=list()
    for line in a:
        if line.find('"') != -1:
            a = line.split(' ')
            for i in a:
                c = i.strip('"')
                c = c.strip(':')
                c = c.strip('"\n')
                c = c.strip(',\n')
                c = c.strip('"')
                lista.append(c)
    dic={}
    dic2={}
    for i in range(len(lista)):
        if lista[i].find('eth') != -1:
            nombre.append(lista[i])
        elif lista[i].find('.') != -1:
            lista2.append(lista[i])
        else:
            lista3.append(lista[i])
    for i in range(len(lista3)):
        dic[lista3[i]]=lista2[i]
    for i in nombre:
        dic2[i]=dic
    return dic2
def main(args):
    dic = leer()
    lista = list()
    for interfaz, datos in dic.items():
        entrada = f"{interfaz}: inet {datos['inet']} netmask {datos['netmask']} broadcastmask {datos['broadcast']}"
        lista.append(entrada)
    print(lista)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
