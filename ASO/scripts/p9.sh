#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    echo "Introduce el nombre para el nuevo usuario: "
    read usuario
    useradd -m "$usuario"
    echo "Introduce la contraseña de usuario: "
    read pass
    echo "$usuario:$pass" | sudo chpasswd
    echo "Usuario '$usuario' creado exitosamente."
}

opcion2() {
    echo "Introduce el nombre del usuario que quieres modificar: "
    read usuario2
    echo "Introduce la nueva contraseña de usuario: "
    read pass2
    sudo usermod -p "$pass2" "$usuario2"
    echo "Usuario modificado correctamente"
}

opcion3() {
    echo "Introduce el nombre del usuario al que quieres eliminar: "
    read usuario3
    sudo userdel -r "$usuario3"
    echo "Usuario eliminado correctamente"
}

opcion4() {
    sudo apt install finger > /dev/null 2>&1
    echo "Introduce el nombre del usuario del que quiere la información: "
    read usuario4
    finger "$usuario4"
}

opcion5() {
    echo "Introduce el nombre del usuario que quiere modificar: "
    read usuario5
    echo "Introduce el grupo que quiere añadir al usuario: "
    read grupo
    usermod -aG "$grupo" "usuario5"

}

salir() {
    echo "Saliendo del menú..."
    exit 0
}

# Menú
while true; do
    clear
    echo "-------------------------"
    echo "     Menú Principal"
    echo "-------------------------"
    echo "1) Crear usuario, pidiendo el usuario y contraseña por pantalla."
    echo " "
    echo "2) Modificar la contraseña del usuario."
    echo " "
    echo "3) Borrar un usuario."
    echo " "
    echo "4) Muestra información de un usuario dado por pantalla."
    echo " "
    echo "5) Añade un usuario a un grupo dado."
    echo " "
    echo "6) Salir"
    echo "-------------------------"
    echo -n "Selecciona una opción: "
    
    read opcion
    
    case $opcion in
        1) opcion1 ;;
        2) opcion2 ;;
        3) opcion3 ;;
        4) opcion4 ;;
        5) opcion5 ;;
        6) salir ;;
        *) echo "Opción no válida, por favor selecciona una opción entre 1 y 6." ;;
    esac
    
    # Pausa para que el usuario vea el resultado antes de continuar
    read -p "Presiona cualquier tecla para continuar..."
done
