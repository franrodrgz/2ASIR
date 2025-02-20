<?php
require_once('secure.php');
// comentar por qué haces estas cosas
$fromView = str_contains($_SERVER['SCRIPT_NAME'], 'service')? false:true;
sessionCheck($fromView);

function getUser() {
    session_start();
    return array('user' => $_SESSION['user'],'name' => $_SESSION['name'],'type' => $_SESSION['type']);    
}
// $user = getUser();
// $isAdmin = $user['type'];
$isAdmin = (getUser()['type']=='A')? true:false;
if(!$isAdmin) {
    sessionClose();
    gotoURL('index.php','Recurso restringido',$fromView);    
}

?>