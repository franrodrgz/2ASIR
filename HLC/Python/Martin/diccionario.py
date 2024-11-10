clientes = {}
selector=0

while selector!=7:
    print(" ")
    print("===============================")
    print("             MENU")
    print("===============================")
    print(" ")
    print("1- Alta de Cliente")
    print("2- Baja de Cliente")
    print("3- Modificacion de cliente")
    print("4- Buscar cliente por DNI")
    print("5- Listado de clientes")
    print("6- Buscar Clientes por Apellido")
    print("7- Salir")
    print(" ")

    selector = int(input("Introduce la opcion que quieres realizar: "))

    if selector == 1:
        print("Has seleccionado Alta de Cliente")
        dni = input("Ingrese el DNI del cliente: ")
        nombre = input("Ingrese el Nombre del cliente: ")
        apellido1 = input("Ingrese el primer Apellido: ")
        apellido2 = input("Ingrese el segundo Apellido: ")
        edad = int(input("Ingrese la edad: "))

        clientes[dni] = {'Nombre': nombre, 'Apellido1': apellido1, 'Apellido2': apellido2, 'Edad': edad}
        print("Datos del cliente:")
        print(clientes[dni])

    elif selector == 2:
        print("Has seleccionado Baja de Cliente")
        dni = input("Ingrese el DNI del cliente a eliminar: ")
        if dni in clientes:
            del clientes[dni]
            print("El cliente se ha dado de baja")
        else:
            print("No existe un cliente con ese DNI en nuestros registros.")

    elif selector == 3:
        print("Has seleccionado Modificación de cliente")
        dni = input("Ingrese el DNI del cliente a modificar: ")
        if dni in clientes:
            nombre = input("Ingrese el nuevo Nombre del cliente: ")
            apellido1 = input("Ingrese el nuevo primer Apellido: ")
            apellido2 = input("Ingrese el nuevo segundo Apellido: ")
            edad = int(input("Ingrese la nueva edad: "))

            clientes[dni]['Nombre'] = nombre
            clientes[dni]['Apellido1'] = apellido1
            clientes[dni]['Apellido2'] = apellido2
            clientes[dni]['Edad'] = edad

            print("Cliente actualizado: ", clientes[dni])
        else:
            print("No existe un cliente con ese DNI en nuestros registros.")

    elif selector == 4:
        print("Has seleccionado Buscar cliente por DNI")
        dni = input("Ingrese el DNI del cliente a buscar: ")
        if dni in clientes:
            print("Los datos del cliente son:", clientes[dni])
        else:
            print("No existe un cliente con ese DNI en nuestros registros.")

    elif selector == 5:
        print("Has seleccionado Listado de clientes")
        for dni in clientes:
            datos = clientes[dni]
            print("DNI:", dni, "Datos:", datos)

    elif selector == 6:
        print("Has seleccionado Buscar Clientes por Apellido")
        apellido = input("Ingrese el Apellido para buscar: ")
        encontrados = False
        for dni in clientes:
            datos = clientes[dni]
            if datos["Apellido1"] == apellido or datos["Apellido2"] == apellido:
                print("DNI:", dni, "Datos:", datos)
                encontrados = True
        if not encontrados:
            print("No se ha encontrado ningun cliente con ese Apellido")

    elif selector == 7:
        print("Ha salido del programa")
