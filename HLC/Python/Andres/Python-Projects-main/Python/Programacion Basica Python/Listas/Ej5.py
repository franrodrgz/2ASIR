def main(args):
    from decimal import Decimal
    lista=list()
    for i in range(5):
        a=input("Nombre de la asignatura: ")
        b=input("Nota: ")
        tupla=[a,Decimal(b)]
        lista.append((tupla))
    lista.sort(key=lambda x: x[1], reverse=False)
    print("Asignatura---Notas")
    print("--------------------------------")
    for a, n in lista:
        print(a,"---",n)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))