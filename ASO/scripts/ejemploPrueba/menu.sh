#!/bin/bash

# Funciones para las opciones del menú
opcion1() {
    bash ./ges_user.sh  # Este script debe existir en la misma ruta
}

opcion2() {
    # Aquí deberías implementar la opción para modificar la contraseña
    echo "Opción 2: Modificar la contraseña del usuario (todavía no implementado)."
}

opcion3() {
    # Aquí deberías implementar la opción para eliminar un usuario
    echo "Opción 3: Borrar un usuario (todavía no implementado)."
}

opcion4() {
    # Aquí deberías implementar la opción para mostrar la información de un usuario
    echo "Opción 4: Mostrar información de un usuario (todavía no implementado)."
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
    echo "1) Crear usuario, pidiendo el usuario y contraseña por pantalla."
    echo " "
    echo "2) Modificar la contraseña del usuario."
    echo " "
    echo "3) Borrar un usuario."
    echo " "
    echo "4) Muestra información de un usuario dado por pantalla."
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
