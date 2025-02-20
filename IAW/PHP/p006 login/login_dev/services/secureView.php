<?php
require_once('secure.php');
// comentar por qué haces estas cosas
$fromView = str_contains($_SERVER['SCRIPT_NAME'], 'service')? false:true;
sessionCheck($fromView);

function getUser() {
    session_start();
    return array('user' => $_SESSION['user'],'name' => $_SESSION['name'],'type' => $_SESSION['type']);    
}
?>