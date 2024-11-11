def main(args):
    print("Introduce un numero de las siguientes opciones del menu para realizar una cuenta aritmetica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    seleccion = int(input())
    if seleccion == 1:
        print("¡Has Seleccionado la Suma, ahora introduce dos numeros para realizar la cuenta!")
        n1 = int(input())
        n2 = int(input())
        resultado = n1 + n2
        print("Aqui tienes el resultado de la Suma = " + str(resultado))
    elif seleccion == 2:
        print("¡Has Seleccionado la Resta, ahora introduce dos numeros para realizar la cuenta!")
        n1 = int(input())
        n2 = int(input())
        resultado = n1 - n2
        print("Aqui tienes el resultado de la Resta = " + str(resultado))
    elif seleccion == 3:
        print("¡Has Seleccionado la Multiplicacion, ahora introduce dos numeros para realizar la cuenta!")
        n1 = int(input())
        n2 = int(input())
        resultado = n1 * n2
        print("Aqui tienes el resultado de la Multiplicacion = " + str(resultado))
    elif seleccion == 4:
        print("¡Has Seleccionado la Division, ahora introduce dos numeros para realizar la cuenta!")
        n1 = int(input())
        n2 = int(input())
        if n2 != 0:
            resultado = n1 / n2
            print("Aqui tienes el resultado de la Division = " + str(resultado))
        else:
            print("No puedes dividir por cero.")
    else:
        print("No has seleccionado una opcion valida")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

