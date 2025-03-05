def suma(a,b):
    r=a+b
    return r

def resta(a,b):
    r=a-b
    return r

def filtro():
    print("Elige la opcion:")
    print("1. Suma")
    print("2. Resta")
    while r<0 or r>2:
        r=int(input())
    return r
def main(args):
    print("Dame las varibles")
    a=int(input("a:"))
    b=int(input("b:"))
    print("Elige la opcion:")
    print("1. Suma")
    print("2. Resta")
    r=int(input())
    if r==1:
        print(suma(a,b))
    elif r==1:
        print(resta(a,b))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
