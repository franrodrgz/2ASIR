def aprobado(x):
    nombre, nota= x
    if(nota == 8):
        return 0
    elif(nota == 9):
        return 1
    return 2

def main(args):
    lista=[('Filosofia',10),('Fisica',8),('Mates',0),('Latin',9),('Historia',4)]
    lista_aprobados= sorted([x for x in lista if x[1] >= 5],key=aprobado)
    print (lista_aprobados)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))