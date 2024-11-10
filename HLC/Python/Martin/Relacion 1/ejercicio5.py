def main(args):
    print("Programa que cambia de posición los números introducidos")
    n1 = input("Escribe un número: ")
    n2 = input("Escribe el segundo número: ")
    c = n1
    n1 = n2
    n2 = c
    print("Los números intercambiados son:")
    print(n1)
    print(n2)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

