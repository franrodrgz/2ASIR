def main(args):
    print("Introduce una nota para saber a que tipo de calificcion pertenece")
    nota = int(input())
    if nota <= 0:
        print("No has introducido una nota valida")
    elif nota <= 4:
        print("La nota es Insuficiente")
    elif nota == 5:
        print("La nota es Suficiente")
    elif nota == 6:
        print("La nota es Bien")
    elif nota == 7 or nota == 8:
        print("La Nota es Notable")
    elif nota == 9 or nota == 10:
        print("La nota es Sobresaliente")
    else:
        print("No has introducido una nota valida")
    return 0       

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))