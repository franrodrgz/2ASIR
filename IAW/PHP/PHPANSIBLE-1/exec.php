<?php
  print_r($_REQUEST);
  //$size = sizeof($_POST['user']);
  $users = $_POST['user'];
  $passs = $_POST['pass'];

  foreach ($users as $user) {
        echo $user;
    }  
  foreach ($passs as $pass) {
        echo $pass;
    }  

?>