#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    echo "Ejecutando el comando nload. Presiona Ctrl+C para salir."
    nload
}

opcion2() {
    echo "Ejecutando el comando iftop. Presiona 'q' para salir."
    sudo iftop
}

opcion3() {
    echo "Ejecutando el comando slurm. Presiona 'q' para salir."
    slurm
}

opcion4() {
    echo "Redirigiendo la salida del comando nload a un fichero..."

    # Crear un nombre de fichero con la fecha actual
    fecha_actual=$(date '+%Y-%m-%d_%H-%M-%S')
    fichero="nload_output_$fecha_actual.txt"

    # Redirigir la salida de nload al fichero
    nload > "$fichero" 2>&1 &
    echo "La salida del comando nload se está guardando en el fichero: $fichero"

    # Avisar al usuario
    echo "Para detener la grabación, localiza el proceso nload con 'ps' y finalízalo con 'kill'."
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
    echo "1) Ejecutar el comando nload"
    echo " "
    echo "2) Ejecutar el comando iftop."
    echo " "
    echo "3) Ejecutar el comando slurm"
    echo " "
    echo "4) Redireccionar la salida del comando nload a un fichero con la fecha actual"
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
