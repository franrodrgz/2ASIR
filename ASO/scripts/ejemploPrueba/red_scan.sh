#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    # Almacenar en un fichero las conexiones en espera o TIME_WAIT
    netstat -an | grep "TIME_WAIT" > salida_red.txt
    echo "Conexiones en espera (TIME_WAIT) almacenadas en salida_red.txt."
}

opcion2() {
    # Muestra la IP de las conexiones web no seguras
    echo "IP de conexiones web no seguras:"
    # Filtrar las conexiones no seguras (puertos no 443)
    grep ":80" salida_red.txt | awk '{print $5}'
}

opcion3() {
    # Muestra por pantalla el contenido del fichero creado en la opción anterior
    cat salida_red.txt
}

opcion4() {
    # Detectar el sistema operativo e información de puertos en el rango de 192.168.8.12 a 192.168.8.23
    for ip in {12..23}; do
        echo "Escaneando 192.168.8.$ip..."
        # Detectar sistema operativo
        os_info=$(ssh -o ConnectTimeout=5 user@192.168.8.$ip "uname -a" 2>/dev/null)
        if [ $? -eq 0 ]; then
            echo "Sistema operativo en 192.168.8.$ip: $os_info"
        else
            echo "No se puede conectar a 192.168.8.$ip."
        fi
        # Escanear puertos (por ejemplo, puertos 22 y 80)
        nmap -p 22,80 192.168.8.$ip | grep ^"192.168.8.$ip"
    done
}

opcion5() {
    # Muestra la información de un usuario solicitado por pantalla
    echo "Introduce el nombre de usuario:"
    read usuario
    # Mostrar información del usuario
    getent passwd $usuario
    if [ $? -ne 0 ]; then
        echo "El usuario no existe."
    fi
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
    echo "1) Almacena en un fichero, llamado salida_red.txt , las conexiones en espera o TIME_WAIT."
    echo "2) Muestra la IP de las conexiones web no seguras de la información almacenada en salida_red.txt."
    echo "3) Muestra por pantalla el contenido del fichero creado en el punto anterior."
    echo "4) Detectar el sistema operativo e información de puertos de los equipos desde el equipo 192.168.8.12 hasta 192.168.8.23"
    echo "5) Muestra la información de un usuario, cuyo nombre se solicitará por pantalla."
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
        *) 
            echo "Opción no válida, por favor selecciona una opción entre 1 y 6." 
            ;;
    esac
    
    # Pausa para que el usuario vea el resultado antes de continuar
    read -p "Presiona cualquier tecla para continuar..."
done
