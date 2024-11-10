def main(args):
    print("Introduce dos numeros para sumarlos si alguno de ellos es positiv/o")
    n1 = int(input())
    n2 = int(input())
    resultado = n1 + n2
    if n1>=0 or n2>=0:
        print("Hay uno o los dos son positivos, aqui tienes la suma = " + str(resultado))
    else:
        print("Los dos numeros son negativos")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
