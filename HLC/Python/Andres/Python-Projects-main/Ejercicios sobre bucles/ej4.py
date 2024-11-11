def main(args):
    i = int(input())
    b = int(input())
    suma=int(0)
    while i <= b:
        suma += i
        i +=1
        print(suma)
    print(suma)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))