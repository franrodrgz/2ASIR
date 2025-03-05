def main(args):
    frase=input("Introduce tu frase: ")
    invertida = ''

    print("Con segmentacion")
    reverse= frase[::-1]
    print(reverse)

    print("Con bucles")
    for i in frase:
        invertida = i + invertida
    print(invertida)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
