def main(args):
    print("Introduce dos numeros que sean negativos para sumarlos")
    n1 = int(input())
    n2 = int(input())
    resultado = n1 + n2
    if n1<=0 and n2<=0:
        print("Los dos numeros son negativos, aqui tienes la suma = " + str(resultado))
    else:
        print("Hay numeros positivos")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
