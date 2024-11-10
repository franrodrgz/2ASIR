
def main(args):
    a=int(input())
    b=int(input())
    suma=0
    while a<=b:
        suma += a
        a += 1
    suma=suma/b
    print(suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
