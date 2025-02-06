#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    # Solicitar dominio
    echo "Introduce el dominio web al que deseas cortar el tráfico saliente:"
    read dominio

    # Resolver el dominio a IP
    ip_dominio=$(dig +short $dominio | head -n 1)

    if [ -z "$ip_dominio" ]; then
        echo "No se pudo resolver el dominio."
        return
    fi

    # Cortar el tráfico saliente hacia la IP del dominio usando iptables
    sudo iptables -A OUTPUT -d $ip_dominio -j DROP
    echo "El tráfico saliente hacia $dominio ($ip_dominio) ha sido bloqueado."
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
