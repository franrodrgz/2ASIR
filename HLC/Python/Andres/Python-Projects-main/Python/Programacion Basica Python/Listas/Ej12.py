def main(args):
    print("Componentes del primer vector")
    u1=int(input("u1: "))
    u2=int(input("u2: "))
    v1=int(input("v1: "))
    v2=int(input("v2: "))
    u=[u1,u2]
    v=[v1,v2]
    k=u[0]/u[1]
    r=v[0]/v[1]
    if k == r:
        print("Los vectores son paralelos")
    else:
        print("Los vectores no son paralelos")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))