def main(args):
    print("Suma de numeros Pares entre el inicio y el final")
    numero1=int(input("Introduce el inicio: "))
    numero2=int(input("Introduce el final: "))
    control=numero1
    suma=0
    while control<=numero2:
        resto = control % 2
        if(resto==0):
           suma=suma+control
        control=control+1
    print(suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
