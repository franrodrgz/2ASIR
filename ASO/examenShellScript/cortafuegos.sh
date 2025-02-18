#!/bin/bash
clear

opcion1() {
    read -p "Introduce la IP que desea bloquear: " $ip1
    iptables –A OUTPUT -s $ip1 –d www.facebook.com –j DROP
}

opcion2() {
    read -p "Introduce la IP de la que desea rechazar los paquetes: " $ip2
    iptables -A INPUT -s $ip2 -d 192.168.8.0/23 –j DROP
}

salir() {
    exit
}

while true; do
    echo "----------------------"
    echo "--- Menu Principal ---"
    echo "----------------------"
    echo "1. Bloquear paquetes de salida de una IP especifica a www.facebook.com."
    echo " "
    echo "2. Rechazar paquetes de un emisor en concreto."
    echo " "
    echo "3. Salir."
    echo "----------------------"
    read -p "Seleccione una opción del 1 al 3: " op

    case $op in
     1) opcion1 ;;
     2) opcion2 ;;
     3) salir ;;

    esac
    read -p "Ctl + C para salir Enter para continuar..."
done
