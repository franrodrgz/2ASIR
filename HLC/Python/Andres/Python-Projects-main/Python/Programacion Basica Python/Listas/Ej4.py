def main(args):
    from decimal import Decimal
    lista=[['Lengua',Decimal('5.6')],['Mates',Decimal('5.6')]]
    lista.sort(key=lambda x: x[1], reverse=False)
    print("Asignatura---Notas")
    print("--------------------------------")
    for a, n in lista:
        print(a,"---",n)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))