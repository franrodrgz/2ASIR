import sys
def main():
    print("Introduce los ingresos")
    a=int(input())
    print("Introduce los gastos")
    b=int(input())
    if a-b>0:
        print("Beneficio")
    elif a-b<0:
        print("Perdida")
    elif a-b==0:
        print("Te quedas igual")
    return 0
if __name__ == '__main__':
    sys.exit(main())
