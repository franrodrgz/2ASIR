<?php
  if(isset($_POST['lamp'])) {
    $lampDomain = $_POST['lampDomain'];
    $lampMysqlRootPass = $_POST['lampMysqlRootPass'];

    $file = 'ansible/lamp.yml';
    $content = file_get_contents($file);

    $content = preg_replace('/mysqlRootPassword:\s*"(.*)"/','mysqlRootPassword: "'.$lampMysqlRootPass.'"',$content);
    $content = preg_replace('/lampDomain:\s*"(.*)"/','lampDomain: "'.$lampDomain.'"',$content);

    file_put_contents($file, $content);

    $command = 'ansible-playbook ansible/lamp.yml -u www-data --skip-tags "mysql-root"';
    $output = shell_exec($command);
    echo "<pre>$output</pre>";      
  }

  if(isset($_POST['ftp'])) {
    $ftpUser = $_POST['ftpUser'];
    $ftpPass = $_POST['ftpPass'];

    $file = 'ansible/vsftpd.yml';
    $content = file_get_contents($file);

    $content = preg_replace('/ftpUser:\s*"(.*)"/','ftpUser: "'.$ftpUser.'"',$content);
    $content = preg_replace('/ftpPass:\s*"(.*)"/','ftpPass: "'.$ftpPass.'"',$content);

    file_put_contents($file, $content);

    $command = 'ansible-playbook ansible/vsftpd.yml -u www-data';
    $output = shell_exec($command);
    echo "<pre>$output</pre>";
  }

  if(isset($_POST['ftp'])) {
    $ftpUser = $_POST['ftpUser'];
    $ftpPass = $_POST['ftpPass'];

    $file = 'ansible/vsftpd.yml';
    $content = file_get_contents($file);

    $content = preg_replace('/ftpUser:\s*"(.*)"/','ftpUser: "'.$ftpUser.'"',$content);
    $content = preg_replace('/ftpPass:\s*"(.*)"/','ftpPass: "'.$ftpPass.'"',$content);

    file_put_contents($file, $content);

    $command = 'ansible-playbook ansible/vsftpd.yml -u www-data';
    $output = shell_exec($command);
    echo "<pre>$output</pre>";
  }
?>