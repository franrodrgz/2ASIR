#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    sudo useradd $1
    echo "$1:$2" | sudo chpasswd
}

opcion2() {
    echo "$1:$2" | sudo chpasswd
}

opcion3() {
    sudo userdel $1
}

opcion4() {
	echo "si"
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
    echo "2) Modificar la contraseña del usuario."
    echo "3) Borrar un usuario."
    echo "4) Dar de alta los usuarios de forma automática leyendo de un fichero. El fichero tendrá separados los campos por ','. En cada fila habrá nombre,DNI,password."
    echo "5) Salir"
    echo "-------------------------"
    echo -n "Selecciona una opción: "
    
    read opcion
    
    case $opcion in
        1) 
            echo "Introduce el nombre para el nuevo usuario: "
            read usuario   
            echo "Introduce la contraseña de usuario: "
            read pass
            opcion1 $usuario $pass
            ;;
        2) 
            echo "Introduce el nombre del usuario que quieres modificar: "
            read usuario2
            echo "Introduce la nueva contraseña de usuario: "
            read pass2
            opcion2 $usuario2 $pass2
            ;;
        3) 
            echo "Introduce el nombre del usuario al que quieres eliminar: "
            read usuario3
            opcion3 $usuario3
            ;;
        4) 
            opcion4 
            ;;
        5) 
            salir 
            ;;
        *) 
            echo "Opción no válida, por favor selecciona una opción entre 1 y 5." 
            ;;
    esac
    
    # Pausa para que el usuario vea el resultado antes de continuar
    read -p "Presiona cualquier tecla para continuar..."
done
