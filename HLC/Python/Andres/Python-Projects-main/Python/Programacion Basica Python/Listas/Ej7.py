def createAlumno(lista):
    a=3
    for i in range(0,a):
        alumno=input("Dame el nombre del alumno ")
        lista.append(alumno)
        createAsignatura(lista,alumno)

def createAsignatura(lista,alumno):
    r=2
    media=0
    for i in range(0,r):
        a=input("Nombre de la asignatura: ")
        b=float(input("Nota: "))
        media += b
        tupla=[a,b]
        lista.append((tupla))
    media=media/r
    print("La media es "+str(media))
    lista.append(media)

def imprimeLista(lista):
    for i in lista:
        if type(i) is str:
            print("Alumno: "+i)
        elif type(i) is float:
            print("La nota media es:"+str(i))
        else:
            a,b=i
            print("Asignatura: "+a)
            print("Nota: "+str(b))
        print("\n")

def main(args):
    lista=list()
    createAlumno(lista)
    print("-------------------------")
    print(lista)
    imprimeLista(lista)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))