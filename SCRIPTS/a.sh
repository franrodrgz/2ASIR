#!/bin/bash
if mount | grep /home/usuario/webAsir > /dev/null; then
  ssh user@192.168.8.198 -p 22 'sudo chmod -R 755 /home/user'
  sudo umount /home/usuario/webAsir
  echo "DesconexiÃ³n realizada correctamente"
else
  ssh user@192.168.8.198 -p 22 'sudo chmod -R 777 /home/user'
  sudo sshfs -p 22 -o IdentityFile=/home/usuario/.ssh/id_rsa,allow_other,default_permissions user@192.168.8.198:/home/user /home/usuario/webAsir/
  echo "ConexiÃ³n realizada con Ã©xito"
fi

