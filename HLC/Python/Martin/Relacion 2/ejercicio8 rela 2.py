def main(args):
    print("Introduce tres numeros para saber cual es el mayor de todos")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    if n1 > n2 and n1 > n3:
        mayor = n1
        print("El numero mayor es el " + str(mayor))
    elif n2 > n1 and n2 > n3:
        mayor = n2
        print("El numero mayor es el " + str(mayor))
    else:
        mayor = n3
        print("El numero mayor es el " + str(mayor))
    return 0
        

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))