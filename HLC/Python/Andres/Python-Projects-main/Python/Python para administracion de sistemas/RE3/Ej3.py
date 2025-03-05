import os

def info():
    print("Usuario actual:", os.getlogin())
    print("Variables de entorno:", os.environ)
    print("Sistema operativo:", os.name)

def main(args):
    info()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))