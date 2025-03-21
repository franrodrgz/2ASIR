#!/bin/bash

while true; do
	echo "-------------------------"
	echo "     Menú Principal"
	echo "-------------------------"
	echo "1. Gestión de Usuarios"
	echo "2. Gestión de la Red"
	echo "3. Salir"
	echo "-------------------------"

  echo "Selecciona una opción: " 
  read opcion

  case $opcion in
    1)
      # Gestión de Usuarios
      echo "Gestión de Usuarios"
      echo "1. Dar de alta usuario manualmente"
      echo "2. Dar de alta usuarios automáticamente (desde un fichero)"
      echo "3. Borrar un usuario"

      echo "Selecciona una opción: "
      read op

      case $op in
        1)
          # Dar de alta usuario manualmente
          echo "Introduce el nombre del usuario: "
          reado usaurio
          sudo useradd $usuario
          echo "Usuario $usuario creado."
          ;;
        2)
          # Dar de alta usuarios automáticamente
          echo "Introduce la ruta del fichero con los nombres de usuarios: "
          read fichero
          while IFS= read -r usuario; do
            sudo useradd $usuario
            echo "Usuario $usuario creado."
          done < "$fichero"
          ;;
        3)
          # Borrar un usuario
          echo "Introduce el nombre del usuario a borrar: "
          read usaurio
          sudo userdel $usuario
          echo "Usuario $usuario eliminado."
          ;;
        *)
          echo "Opción no válida."
          ;;
      esac
      ;;
    2)
      # Gestión de la Red
      echo "Gestión de la Red"
      echo "1. Mostrar dirección IP de conexiones no seguras"
      echo "2. Mostrar conexiones seguras establecidas (protocolo seguro)"
      echo "3. Almacenar conexiones UDP en un fichero"

      echo "Selecciona una opción: "
      read op

      case $op in
        1)
          # Mostrar dirección IP de conexiones no seguras
          echo "Conexiones no seguras (puertos HTTP):"
          netstat -an | grep ':80'
          ;;
        2)
          # Mostrar conexiones seguras establecidas
          echo "Conexiones seguras (puertos HTTPS):"
          netstat -an | grep ':443'
          ;;
        3)
          # Almacenar conexiones UDP en un fichero
          salida="conexiones_udp.txt"
          netstat -anu > "$salida"
          echo "Conexiones UDP almacenadas en $salida"
          ;;
        *)
          echo "Opción no válida."
          ;;
      esac
      ;;
    3)
      echo "Saliendo del programa."
      break
      ;;
    *)
      echo "Opción no válida."
      ;;
  esac
done
