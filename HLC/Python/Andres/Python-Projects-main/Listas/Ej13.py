import math
def main(args):
    print("Componentes del primer vector")
    u1=int(input("u1: "))
    u2=int(input("u2: "))
    u=[u1,u2]
    r=math.sqrt(u[0]+u[1])
    print(r)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))