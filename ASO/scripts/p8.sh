#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    echo "Mostrando los puertos..."
    sudo netstat -tuln
}

opcion2() {
    echo "Indica la dirección de red: "
    read red
    sudo nmap -sn $red
}

opcion3() {
    echo "Indica la dirección de red: "
    read host
    echo "Detectando SO de $host..."
    # Usar nmap para detectar el sistema operativo
    sudo nmap -O $host
}

opcion4() {
    echo "Indica la dirección de red: "
    read red
    sudo nmap -sn $red > salida_host.txt
    sudo netstat -tuln >> salida_host.txt
}

opcion5() {
    echo "Introduce la informacíon que deseas buscar: "
    read info
    cat salida_host.txt | grep "$info"
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
    echo "1) Muestra el estado de los puertos, con su protocolo de los host de tu red."
    echo " "
    echo "2) Muestra los hosts activos de tu red."
    echo " "
    echo "3) Identifca los Sistemas operativos de los hosts de tu red."
    echo " "
    echo "4) Manda la información de los puntos 1 y 3 a un fichero salida_host.txt."
    echo " "
    echo "5) Busca toda la información relativa a un host, cuya IP solicitaras por pantalla en el fichero salida_host.txt."
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
