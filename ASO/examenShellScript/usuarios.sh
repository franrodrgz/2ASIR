#!/bin/bash

opcion1() {
    read -p "Introduce el nombre del usuario a crear: " usuario
    sudo useradd -m -d /home/$usuario -s /bin/bash $usuario
}

opcion2() {
    cat /etc/passwd > usur.txt
}

salir() {
    exit
}

while true; do
    echo "----------------------"
    echo "--- Menu Principal ---"
    echo "----------------------"
    echo "1. Dar de alta a un usuario."
    echo " "
    echo "2. Mostrar los usuarios del sistema."
    echo " "
    echo "3. Salir."
    echo "----------------------"
    read -p "Seleccione una opción del 1 al 3: " op

    case $op in
     1) opcion1 ;;
     2) opcion2 ;;
     3) salir ;;

    esac
done
