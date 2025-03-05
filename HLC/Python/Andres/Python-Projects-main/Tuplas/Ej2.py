#Coger los datos de un usuario y delvolver la ip
def getUser():
    nombre=input("Introduce el nombre del usuario: ")
    apellido=input("Introduce el apellido del usuario: ")
    ip=input("Introduce la IP del usuario:")
    u = (nombre,apellido,ip)
    return u[2]


def main(args):
    print("La ip es", getUser())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
