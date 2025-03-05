import sys
def leer():
    try:
        a = open("Ej7.txt")
    except FileNotFoundError:
        print ("No se puede abrir el archivo")
    listadic = list()
    dic ={}
    dic2={}
    for i in a:
        if i.find("'") != -1:
            lista = i.split(" ")
            dic = {}
            dic["filesytem"]=lista[0].strip("'")
            dic["size"]=lista[1]
            dic["available"]=lista[2]
            dic["mounted"]=lista[3]
            dic["Used"]=lista[4]
            dic["On"]=lista[5].strip("'\n")
            listadic.append(dic)
    return listadic

def busqueda(listadic):
    b=input("Cual quieres consultar")
    print(b)
    for i in range(len(listadic)):
        if b in listadic[i]["filesytem"]:
            print(listadic[i])

def tupla(listadic):
    listatupla = []
    for i in range(len(listadic)):
        tupla = (listadic[i]["filesytem"],listadic[i]["size"])
        listatupla.append(tupla)
    print(listatupla)

def tupla2(listadic):
    listatupla = []
    filtro = input("Porcentaje: ")
    for i in range(len(listadic)):
        if listadic[i]["Used"] >= filtro:
            tupla = (listadic[i]["filesytem"],listadic[i]["size"])
            listatupla.append(tupla)
    print(listatupla)

def main(args):
    listadic = leer()
    busqueda(listadic)
    #tupla(listadic)
    tupla2(listadic)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
