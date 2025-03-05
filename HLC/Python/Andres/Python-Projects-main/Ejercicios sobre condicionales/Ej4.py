import sys
def main():
    print("Introduce los ingresos")
    a=int(input())
    print("Introduce los gastos")
    b=int(input())
    if a-b>0:
        print("Beneficio")
    else:
        print("Perdida")
    return 0
if __name__ == '__main__':
    sys.exit(main())