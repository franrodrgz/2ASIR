import sys
import ast
def lectura():
    try:
        a=open("rel1.txt")
    except FileNotFoundError:
        print("Archivo no encontrado")
    name=list()
    proceso=list()
    valor=list()
    valores=list()
    lista=list()
    b=0
    for x in a:
        if x.find('":') != -1:
            if x.find('": {') != -1:
                x=x.split('"')
                name.append(x[1])
            elif x.find('": [') != -1:
                x=x.split('"')
                c=x[2].split('[')
                c=c[1].split(', ')
                for i in c:
                    lim=i.strip('],\n')
                    valor.append(lim)
                valores.append(valor)
                valor=[]
                proceso.append(x[1])
        elif x.find('},') != -1:
            lista.append(proceso)
            proceso=[]
            b+=1
        elif x.find('}\n') != -1:
            lista.append(proceso)
            proceso=[]
            b+=1

    diccionario = {}
    dic2={}
    a = 0
    c = 0
    for i in lista:
        diccionario = {}
        for j in i:
            diccionario[j] = valores[c]
            c+=1
        dic2[name[a]] = diccionario
        a +=1
    #diccionario = ast.literal_eval(contenido)
    #print(diccionario["SRV001"]["WebServer"])

    return dic2

def dictCreate(a):
    listab = []
    q={}
    n=0
    for key,values in a.items():
        for value in values:
            c=0
            d=0
            b = a[key][value]
            for i in b:
                c+=int(i)
                d+=1
            listab.append(c/d)
    for key,values in a.items():
        for value in values:
            print(value)
            a[key][value] = listab[n]
            print(listab[n])
            n+=1
    print(a)
    return 0

def main(args):
    b=lectura()
    dictCreate(b)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))