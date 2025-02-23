#!/bin/bash
if mount | grep /home/usuario/webAsir > /dev/null; then
  ssh user@vb -p 22 'sudo chmod -R 755 /var/www/html'
  sudo umount /home/usuario/webAsir
  echo "DesconexiÃ³n realizada correctamente"
else
  ssh user@vb -p 22 'sudo chmod -R 777 /var/www/html'
  sudo sshfs -p 22 -o IdentityFile=/home/usuario/.ssh/id_rsa,allow_other,default_permissions user@vb:/var/www/html /home/usuario/webAsir/
  echo "ConexiÃ³n realizada con Ã©xito"
fi

