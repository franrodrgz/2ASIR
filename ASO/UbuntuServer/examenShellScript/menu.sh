#!/bin/bash

opcion1() {
    bash ./scan.sh
}

opcion2() {
    bash ./cortafuegos.sh
}

opcion3() {
    bash ./usuarios.sh
}

salir() {
    exit
}

while true; do
    echo "----------------------"
    echo "--- Menu Principal ---"
    echo "----------------------"
    echo "1. Red."
    echo " "
    echo "2. Seguridad."
    echo " "
    echo "3. Gestión de Usuarios."
    echo " "
    echo "4. Salir."
    echo "----------------------"
    read -p "Seleccione una opción del 1 al 4: " op

    case $op in
     1) opcion1 ;;
     2) opcion2 ;;
     3) opcion3 ;;
     4) salir ;;

    esac
done
