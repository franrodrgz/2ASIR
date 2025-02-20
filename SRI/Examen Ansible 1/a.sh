#!/bin/bash
#Instalar Nginx
ansible-playbook playbook2.yml -i inventario -u user
#Intalar los apaches
read -p "Cuantos servidores de apache vas a instalar" veces
for ((i=1; i<=veces; i++))
do
    echo "Instalacion de apache numero $i"
    ansible-playbook playbook.yml -i inventario -u user
done
