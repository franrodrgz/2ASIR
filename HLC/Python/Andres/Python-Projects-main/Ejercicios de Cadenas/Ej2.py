
def main(args):
    frase=input("Introduce tu frase: ")
    b=0
    for i in frase:
        if i == " ":
            b+=1
    print("Espacios contados")
    i=frase.count(" ")
    print(i)
    print(b)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
