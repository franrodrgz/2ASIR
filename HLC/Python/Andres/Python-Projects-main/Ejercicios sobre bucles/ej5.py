
def main(args):
    a=int(input())
    b=int(input())
    suma=0
    while a <= b:
        if a % 2 == 0:
            suma += a
        a += 1
        print(suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
