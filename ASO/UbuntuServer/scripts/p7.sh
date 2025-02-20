#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    echo "Introduce la dirección IP de tu servidor: "
    read ipserver
    sudo iptables -A INPUT -s $ipserver -j DROP
    echo "Regla actualizada, aplicando persistencia..."
    sudo /sbin/iptables-save
    echo "La regla ahora es persistente."
}

opcion2() {
    echo "Introduce el rango de tu red a los que le quieres realizar la configuración, la sintaxis será (IP1-IP2): "
    read iprange
    sudo iptables -A OUTPUT -m iprange --src-range $iprange -j REJECT
    echo "Regla actualizada, aplicando persistencia..."
    sudo /sbin/iptables-save
    echo "La regla ahora es persistente."
}

opcion3() {
    echo "Introduce la dirección de tu red la sintaxis será (IP/Máscara de red): "
    read ipred
    sudo iptables -A OUTPUT -d www.facebook.com -s $ipred -j DROP
    echo "Regla actualizada, aplicando persistencia..."
    sudo /sbin/iptables-save
    echo "La regla ahora es persistente."
}

opcion4() {
    echo "Actualizando repositorios"
    sudo apt update
    clear
    echo "Repositorios actualizados con exito, instalando IPTABLES."
    sudo apt install iptables
    clear
    echo "IPTABLES instalado con exito."
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
    echo "1) Haga un filtro de paquetes entrantes de forma que ningún equipo del exterior pueda acceder al servidor"
    echo " "
    echo "2) Realiza un filtro de paquetes salientes de forma que lo pcs de la clase no puedan acceder al exterior."
    echo " "
    echo "3) Realizar un filtrado de paquetes salientes para que ningún equipo pueda acceder al dominio www.facebook.com"
    echo " "
    echo "4) Instalar IPTABLES."
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
