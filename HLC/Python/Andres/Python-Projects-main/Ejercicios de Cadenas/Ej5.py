def division(b):
    a= int(b[0])/int(b[1])
    r= "El resultado de la fraccion es "+str(a)
    return r
def main(args):
    frase=input("Introduce la fraccion: ")
    b=frase.split("/")
    print(b)
    print(division(b))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
