#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    echo "Que nombre desea darle al fichero"
    read nombre
    history > "$nombre"
    echo "El historial de comandos se ha guardado en el archivo: $nombre"
}

opcion2() {
    echo "Este es el contenido de $nombre"
    cat $nombre
}

opcion3() {
    echo "Introduce el nombre de usuario nuevo: "
    read usuario
    useradd -m -d /home/$usuario -s /bin/bash $usuario
    echo "Usuario creado"
    echo "Introduce una contraseña para el usuario..."
    passwd $usuario
}

opcion4() {
    ls /home/usuario
}

salir() {
    echo "Saliendo del menú..."
    exit 0
}

# Menú
while true; do
    clear
    echo "-------------------------"
    echo "   Menú Principal"
    echo "-------------------------"
    echo "1) Almacenar el historial de tu pc en un fichero, cuyo nombre solicitarás al usuario"
    echo "2) Muestra por pantalla el contenido del fichero creado en el punto 1."
    echo "3) Ejecuta el shell scritp crear_usuario.sh, el cual pedirá por pantalla el nombre  y contraseña de un nuevo usuario y lo creará."
    echo "4) Muestra el contenido de tu carpeta personal."
    echo "5) Salir"
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
