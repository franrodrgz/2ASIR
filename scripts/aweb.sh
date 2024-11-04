#!/bin/bash
if mount | grep /home/usuario/shared/vb1 > /dev/null; then
  ssh user@vb1 -p 22 'sudo chmod -R 755 /var/www/html'
  sudo umount /home/usuario/shared/vb1
  echo "Desconexión realizada correctamente"
else
  ssh user@vb1 -p 22 'sudo chmod -R 777 /var/www/html'
  sudo sshfs -p 22 -o IdentityFile=/home/usuario/.ssh/id_rsa,allow_other,default_permissions user@vb1:/var/www/html /home/usuario/shared/vb1/
  echo "Conexión realizada con éxito"
fi
