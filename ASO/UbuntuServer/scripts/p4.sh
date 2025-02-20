#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    echo "Mostrando y analizando conexiones de red..."
    echo "Guardando todas las conexiones en salidaNetstat.txt..."
    netstat -ant > salidaNetstat.txt
    echo "Se ha guardado la salida en salidaNetstat.txt."
}

opcion2() {
    echo "Filtrando conexiones ESTABLISHED..."
    grep "ESTABLISHED" salidaNetstat.txt > salidaNetstatEstablecido.txt
    echo "Conexiones ESTABLISHED guardadas en salidaNetstatEstablecido.txt."
}

opcion3() {
    echo "Contando conexiones por estado..."
    conexiones_establecidas=$(grep -c "ESTABLISHED" salidaNetstat.txt)
    conexiones_time_wait=$(grep -c "TIME_WAIT" salidaNetstat.txt)
    echo "Conexiones ESTABLISHED: $conexiones_establecidas"
    echo "Conexiones TIME_WAIT: $conexiones_time_wait"
}

opcion4() {
    echo "Extrayendo IPs de conexiones web no seguras (puerto 80)..."
    grep ":80" salidaNetstat.txt | awk '{print $5}' | cut -d':' -f1 | sort -u > ipsNoSeguras.txt
    echo "IPs de conexiones web no seguras guardadas en ipsNoSeguras.txt."
    echo "IPs no seguras encontradas:"
    cat ipsNoSeguras.txt
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
    echo "1) Muestra las conexiones de tu red y guarda la salida en un fichero salida-netstat.txt (Usa para ello el comando netstat)"
    echo " "
    echo "2) Haz un filtro del fichero salida-netstat.txt cogiendo únicamente las líneas de las conexiones ESTABLECIDAS. Guarda la salida en un fichero llamado salida-netstat-establecido.txt."
    echo " "
    echo "3) Muestra por pantalla cuantas conexiones están ESTABLECIDO y cuantas en TIME_WAIT. Hay un comando en bash para contar líneas en ficheros."
    echo " "
    echo "4) Muestra la ip de la conexiones web no seguras."
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
