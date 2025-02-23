#!/bin/bash

opcion1() {
    netstat | grep "TIME_WAIT" > salida_red.txt
}

opcion2() {
    cat ./salida_red.txt | grep "http"
}

opcion3() {
    sudo nmap -sV -O 192.168.8.45-80
}

salir() {
    exit
}

while true; do
    echo "----------------------"
    echo "--- Menu Principal ---"
    echo "----------------------"
    echo "1. Fichero con las conexiones en espera."
    echo " "
    echo "2. Conexiones no seguras a la web."
    echo " "
    echo "3. Detectar SO e informacion de puertos de un rango de IPs."
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
    read -p "Desea Continuar S/N?" yn
done
