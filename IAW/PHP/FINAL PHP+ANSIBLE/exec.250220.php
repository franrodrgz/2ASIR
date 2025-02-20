<?php
$users = $_POST['user'];
$passs = $_POST['pass'];

$size = sizeof($users);

if($size>0) {
  $file = 'ansible/vsftpd.yml';
  $content = file_get_contents($file);

  // Expresiones regulares para reemplazar valores
  $user = $_POST['user'];
  $pass = $_POST['pass'];

  $content = preg_replace('/option:\s*"(.*)"/','option: "'.$size.'"',$content);
  $content = preg_replace('/ftpUser1:\s*"(.*)"/','ftpUser1: "'.$user.'"',$content);
  $content = preg_replace('/ftpPass1:\s*"(.*)"/','ftpPass1: "'.$pass.'"',$content);

  if($size == 2) {
    $content = preg_replace('/ftpUser2:\s*"(.*)"/','ftpUser2: "'.$user.'"',$content);
    $content = preg_replace('/ftpPass2:\s*"(.*)"/','ftpPass2: "'.$pass.'"',$content);
  }

  file_put_contents($file, $content);
  /*
  $command = 'ansible-playbook ansible/vsftpd.yml -u www-data';
  exec($command, $output, $return_var);

  if ($return_var !== 0) {
      echo "Error en la ejecución (Código: $return_var)";
      echo "<pre>".implode("\n", $output)."</pre>";
  } else {
      echo "Ejecución exitosa";
  }
  */
  // Comando de Ansible (ej: listar hosts)
  $command = 'ansible-playbook ansible/vsftpd.yml -u www-data';

  // Ejecutar y capturar la salida
  $output = shell_exec($command);

  // Mostrar resultados
  echo "<pre>$output</pre>";  
}
?>