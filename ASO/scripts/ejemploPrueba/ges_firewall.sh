#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
   echo "Introduce el dominio al cual deseas cortar el tráfico saliente (ejemplo: ejemplo.com):"
    read dominio

    # Comprobar si el dominio es válido resolviendo la IP
    sudo ip_dominio=$(getent hosts "$dominio" | awk '{ print $1 }')
    if [ -z "$ip_dominio" ]; then
        echo "No se pudo resolver el dominio $dominio."
        return
    fi

    echo "Cortando el tráfico saliente hacia $dominio ($ip_dominio)..."

    # Usar iptables para cortar el tráfico saliente hacia el dominio
    sudo iptables -A OUTPUT -d "$ip_dominio" -j REJECT
    if [ $? -eq 0 ]; then
        echo "Tráfico saliente hacia $dominio ($ip_dominio) ha sido cortado."
    else
        echo "Error al cortar el tráfico."
    fi
}

opcion2() {
    # Solicitar la IP del servidor
    echo "Introduce la IP de tu servidor al que deseas cortar el tráfico entrante:"
    read ip_servidor

    # Cortar el tráfico entrante hacia la IP del servidor usando iptables
    sudo iptables -A INPUT -d $ip_servidor -j DROP
    echo "El tráfico entrante hacia el servidor $ip_servidor ha sido bloqueado."
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
    echo "1) Cortar el tráfico saliente hacia un dominio web solicitado por pantalla."
    echo "2) Cortar el tráfico entrante hacia nuestro Servidor (la IP se solicitará por pantalla)."
    echo "3) Salir"
    echo "-------------------------"
    echo -n "Selecciona una opción: "
    
    read opcion
    
    case $opcion in
        1) opcion1 ;;
        2) opcion2 ;;
        3) salir ;;
        *) 
            echo "Opción no válida, por favor selecciona una opción entre 1 y 3." 
            ;;
    esac
    
    # Pausa para que el usuario vea el resultado antes de continuar
    read -p "Presiona cualquier tecla para continuar..."
done
