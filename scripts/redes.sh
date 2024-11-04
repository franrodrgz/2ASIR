#!/bin/bash
if mount | grep /home/usuario/shared/vb1 > /dev/null; then
  ssh user@192.168.59.43 -p 22 'sudo chmod -R 755 /home/user'
  sudo umount /home/usuario/shared/vb1
  echo "Desconexión realizada correctamente"
else
  ssh user@192.168.59.43 -p 22 'sudo chmod -R 777 /home/user'
  sudo sshfs -p 22 -o IdentityFile=/home/usuario/.ssh/id_rsa,allow_other,default_permissions user@192.168.59.43:/home/user /home/usuario/shared/vb1/
  echo "Conexión realizada con éxito"
fi
