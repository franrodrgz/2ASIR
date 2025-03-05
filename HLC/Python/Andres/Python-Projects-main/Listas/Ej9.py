def countA(lista):
    a="a"
    lista=lista.lower()
    count=0
    for i in lista:
        if a == i:
            count+=1
    return count

def countE(lista):
    e="e"
    lista=lista.lower()
    count=0
    for i in lista:
        if e == i:
            count+=1
    return count

def main(args):
    frase=input("Introduce tu frase: ")
    print("Recuento de vocales")
    print("================================================================")
    print("Vocal a:",countA(frase))
    print("Vocal e:",countE(frase))
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))