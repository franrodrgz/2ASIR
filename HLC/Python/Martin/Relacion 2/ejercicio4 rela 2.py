def main(args):
    print("Introduce los Ingresos y los gastos para saber si ha habido Ganancias o Perdidas")
    ingreso = int(input())
    gasto = int(input())
    resultado = ingreso - gasto
    if resultado>0:
        print("Has obtenido ganancias")
    else:
        print("Has tenido perdidas")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
