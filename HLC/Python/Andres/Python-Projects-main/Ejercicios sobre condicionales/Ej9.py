import sys
def main():
    print("Introduce un numero")
    a=int(input())
    print("Introduce otro un numero")
    b=int(input())
    print("Introduce otro un numero")
    c=int(input())
    if a>=b and a>=c:
        if b>=c:
            print(a,b,c)
        else:
            print(a,c,b)
    elif b>=a and b>=c:
        if a>=c:
            print(b,a,c)
        else:
            print(b,c,a)
    else:
        if a>=b:
            print(c,a,b)
        else:
            print(c,b,a)
    return 0
if __name__ == '__main__':
    sys.exit(main())