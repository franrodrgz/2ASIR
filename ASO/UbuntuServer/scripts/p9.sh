#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    sudo useradd -m "$1"
    sudo echo "$1:$2" | sudo chpasswd
    echo "Usuario '$1' creado exitosamente."
}

opcion2() {
    sudo usermod -p "$2" "$1"
    echo "Usuario modificado correctamente"
}

opcion3() {
    sudo userdel -r "$1"
    echo "Usuario eliminado correctamente"
}

opcion4() {
    sudo apt install finger > /dev/null 2>&1
    finger "$1"
}

opcion5() {
    sudo usermod -aG "$2" "$1"
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
        1) 
	echo "Introduce el nombre para el nuevo usuario: "
	read usuario   
	echo "Introduce la contraseña de usuario: "
	read pass
        opcion1 $usuario $pass;;
        2) 
    	echo "Introduce el nombre del usuario que quieres modificar: "
    	read usuario2
    	echo "Introduce la nueva contraseña de usuario: "
    	read pass2
        opcion2 $usuario2 $pass2;;
        3) 
        echo "Introduce el nombre del usuario al que quieres eliminar: "
        read usuario3
        opcion3 $usuario3;;
        4) 
        echo "Introduce el nombre del usuario del que quiere la información: "
        read usuario4
        opcion4 $usuario4;;
        5) 
        echo "Introduce el nombre del usuario que quiere modificar: "
    	read usuario5
   	 echo "Introduce el grupo que quiere añadir al usuario: "
    	read grupo
        opcion5 $usuario5 $grupo;;
        6) salir ;;
        *) echo "Opción no válida, por favor selecciona una opción entre 1 y 6." ;;
    esac
    
    # Pausa para que el usuario vea el resultado antes de continuar
    read -p "Presiona cualquier tecla para continuar..."
done
