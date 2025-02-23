#!/bin/bash
if mount | grep /home/usuario/webAsir > /dev/null; then
  ssh user@1 -p 22 'sudo chmod -R 755 /var/www/html'
  sudo umount /home/usuario/webAsir
  echo "Desconexión realizada correctamente"
else
  ssh user@1 -p 22 'sudo chmod -R 777 /var/www/html'
  sudo sshfs -p 22 -o IdentityFile=/home/usuario/.ssh/id_rsa,allow_other,default_permissions user@1:/var/www/html /home/usuario/webAsir/
  echo "Conexión realizada con éxito"
fi
