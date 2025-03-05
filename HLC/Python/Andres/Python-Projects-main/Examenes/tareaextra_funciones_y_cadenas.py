#Construye una función que recibe una tupla con cuatro elementos (nombre,hostname,ip,email) y devuelve el email
#Construye una función que recibe una cadena de caracteres con un email y devuelve el dominio.
#Construye un programa que usa las funciones anteriores para mostrar por pantalla el dominio del email de un usuario
def createUser():
    nombre = input("Introduce el nombre del usuario: ")
    hostname = input("Introduce el hostname: ")
    ip = input("Introduce la ip: ")
    email = input("Introduce el email: ")
    return (nombre, hostname, ip, email)

def dominio(email):
    dominio = email.split("@")
    return dominio[1]

def main(args):
    tupla = createUser()
    tupla2 = createUser()
    print("El dominio es",dominio(tupla[3]))
    print("El dominio es",dominio(tupla2[3]))
    return 0
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
