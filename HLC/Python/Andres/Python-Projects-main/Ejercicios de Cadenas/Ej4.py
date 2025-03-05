def main(args):
    frase=input("Introduce tu frase: ")
    a=input("Introduce el caracter que vamos a contar: ")
    c=0
    for i in frase:
        if i == a:
            c+=1
    print("Hay",a,"en la frase")
    print(c)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
