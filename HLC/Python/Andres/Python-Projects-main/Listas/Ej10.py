def main(args):
    print("Componentes del primer vector")
    u1=int(input("u1: "))
    u2=int(input("u2: "))
    v1=int(input("v1: "))
    v2=int(input("v2: "))
    k=u1*v1+u2*v2
    print(f"El producto escalar es: {k}")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))