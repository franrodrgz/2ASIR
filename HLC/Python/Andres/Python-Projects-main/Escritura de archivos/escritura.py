def escribe(b):
    try:
        a=open("a.txt","w")
    except FileNotFoundError:
        print("Archivo no encontrado")
    a.write(b)
    print("Hecho")

def main(args):
    escribe("hola")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))