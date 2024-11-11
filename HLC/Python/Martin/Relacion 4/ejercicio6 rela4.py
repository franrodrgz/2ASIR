def main(args):
    suma=0
    for numbers in range(10):
        numero=int(input("Introduce un numero: "))
        suma=suma+numero
    promedio=suma/10
    print(promedio)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))