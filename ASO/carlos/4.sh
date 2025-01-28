#!/bin/bash
opcion=0

while [ $opcion -ne 5 ]
do
    clear
    echo "1.Muestra las conexiones de tu red y guarda la salida en un fichero salida-netstat.txt (Usa para ello el comando netstat)"
    echo "2.Haz un filtro del fichero salida-netstat.txt cogiendo únicamente las líneas de las conexiones ESTABLECIDAS. Guarda la salida en un fichero llamado salida-netstat-establecido.txt."
    echo "3.Muestra por pantalla cuantas conexiones están ESTABLECIDO y cuantas en TIME_WAIT. Hay un comando en bash para contar líneas en ficheros."
    echo "4.Muestra la ip de la conexiones web no seguras."
    echo "5.Salir"
    read -p "Selecciona una opción: " opcion

    case $opcion in
        1)
            echo "Mostrando y analizando conexiones de red..."
            echo "Guardando todas las conexiones en salida-netstat.txt..."
            netstat -ant > salida-netstat.txt
            echo "Se ha guardado la salida en salida-netstat.txt."
        2)
            echo "Filtrando conexiones ESTABLISHED..."
            grep "ESTABLISHED" salida-netstat.txt > salida-netstat-establecido.txt
            echo "Conexiones ESTABLISHED guardadas en salida-netstat-establecido.txt."

        3)
            echo "Contando conexiones por estado..."
            conexiones_establecidas=$(grep -c "ESTABLISHED" salida-netstat.txt)
            conexiones_time_wait=$(grep -c "TIME_WAIT" salida-netstat.txt)
            echo "Conexiones ESTABLISHED: $conexiones_establecidas"
            echo "Conexiones TIME_WAIT: $conexiones_time_wait"

        4)
            echo "Extrayendo IPs de conexiones web no seguras (puerto 80)..."
            grep ":80" salida-netstat.txt | awk '{print $5}' | cut -d':' -f1 | sort -u > ips-no-seguras.txt
            echo "IPs de conexiones web no seguras guardadas en ips-no-seguras.txt."
            echo "IPs no seguras encontradas:"
            cat ips-no-seguras.txt

            read -p "Pulsa una tecla para continuar..."
        ;;
        5)
            echo "¡Adiós!"
        ;;
        *)
            echo "Opción no válida. Intente de nuevo."
            read -p "Pulsa una tecla para continuar..."
        ;;
    esac
done
