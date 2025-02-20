#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    bash ./ges_user.sh  # Este script debe existir en la misma ruta
}

opcion2() {
    bash ./red_scan.sh
}

opcion3() {
    bash ./ges_firewall.sh
}

opcion4() {
    sudo lpstat -a
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
    echo "1) ges_user.sh."
    echo " "
    echo "2) red_scan.sh."
    echo " "
    echo "3) ges_firewall.sh."
    echo " "
    echo "4) Mostrar la impresoras disponibles en nuestro sistema."
    echo " "
    echo "5) Salir"
    echo "-------------------------"
    echo -n "Selecciona una opción: "
    
    read opcion
    
    case $opcion in
        1) opcion1 ;;
        2) opcion2 ;;
        3) opcion3 ;;
        4) opcion4 ;;
        5) salir ;;
        *) echo "Opción no válida, por favor selecciona una opción entre 1 y 5." ;;
    esac
    
    # Pausa para que el usuario vea el resultado antes de continuar
    read -p "Presiona cualquier tecla para continuar..."
done
