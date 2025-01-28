#!/bin/bash
opcion=0

while [ $opcion -ne 4 ]
do
    clear
    echo "1. Crear archivo comprimido con la fecha"
    echo "2. Solicitar archivo para hacerlo ejecutable"
    echo "3. Redirigir un archivo log a un .txt, solicitar el nombre por pantalla"
    echo "4. Salir"
    read -p "Selecciona una opcion: " opcion

    case $opcion in
        1)
            echo "Creando archivo comprimido con la fecha..."
            fecha=$(date +%Y-%m-%d)
            archivo_comprimido="archivo_$fecha.tar.gz"
            echo "Creando archivo: $archivo_comprimido"
            tar -czf $archivo_comprimido * 2>/dev/null
            echo "Archivo comprimido correctamente."
            read -p "Pulsa una tecla para continuar..."
        ;;
        2)
            echo "Introduce el nombre del fichero"
            read nombre
            if [ -f "$nombre" ]; then
                chmod +x "$nombre"
                echo "El archivo $nombre ahora es ejecutable."
            else
                echo "El archivo $nombre no existe o no está en esta carpeta."
            fi
            read -p "Pulsa para continuar..."
        ;;
        3)
            echo "Redirigiendo el archivo a .txt"
            echo "Introduce el nombre del archivo log."
            read log
            if [ -f "$log" ]; then
                archivo="${log%.*}.txt"
                cat "$log" > "$archivo"
                echo "Contenido redirigido a $archivo."
                
                op=0
                while [ $op -ne 2 ]
                do
                    echo "¿Quieres ver el contenido del archivo?"
                    echo "1. Sí"
                    echo "2. No"
                    read -p "Selecciona una opción: " op
                    case $op in
                        1)
                            echo "Mostrando información: "
                            cat $archivo
                            read -p "Pulsa para continuar..."
                        ;;
                        2)
                            read -p "Pulsa para continuar..."
                        ;;
                        *)
                            echo "Opción no válida."
                            read -p "Pulsa para continuar..."
                        ;;
                    esac
                done
            else
                echo "El archivo $log no existe."
            fi
            read -p "Pulsa para continuar..."
        ;;
        4)
            echo "¡Adiós!"
        ;;
        *)
            echo "Opción no válida. Intente de nuevo."
            read -p "Pulsa para continuar..."
        ;;
    esac
done
