def main(args):
    frase=input("Introduce tu frase: ")
    print("Hecho con range")
    for i in range(0,len(frase)):
        print(frase[i])
    print("Hecho con la caracteristica iterable de las cadenas")
    for i in frase:
        print(i)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
