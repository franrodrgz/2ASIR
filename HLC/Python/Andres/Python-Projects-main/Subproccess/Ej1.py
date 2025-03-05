import os

def navegacion_y_creacion():
    print("Directorio actual:", os.getcwd())
    os.chdir("/tmp")
    print("Cambiado a:", os.getcwd())
    os.mkdir("practica")
    print("Contenido de /tmp:", os.listdir("/tmp"))

def main(args):
    navegacion_y_creacion()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))