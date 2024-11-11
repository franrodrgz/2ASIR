def main(args):
    a=int(input("Introduce el numero del que quieres calcular el factorial \n"))
    i=1
    mul=1
    for i in range(i,a+1):
        mul*=i
    print(mul)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))