<?php

require_once('../dao/mysql.php');
require_once('../services/basic.php');

function createSession($user, $name, $type='U') {
    $id = ($type=='U')? 'Z~LY<?7RJ^s#CB6K]w-2cM':'qa]+HjE7_26>-sZU;"8w.m';
    session_start();
    session_id($id);
    $_SESSION['user'] = $user;
    $_SESSION['name'] = $name;
    $_SESSION['type'] = $type;
}


$op = $_REQUEST['op'];

switch ($op) {
    case 'in':
        $link = getLink();
        $user = $_POST['mail'];
        $pass = $_POST['pass'];
        $query = "SELECT users.* FROM users WHERE users.user='$user'";
        $result = mysqli_query($link, $query);
        mysqli_close($link);        
        $row = mysqli_fetch_assoc($result);
        mysqli_free_result($result);
        if(password_verify($pass, $row['pass'])) {
            createSession($row['user'],$row['name'],$row['type']);
            $url = 'start.php';
            $msg = 'Bienvenid@ '.$row['name'];
        } else {
            $url = 'index.php';
            $msg = 'Contraseña o usuario incorrectos';
        }
        goToURL($url,$msg);
        break;
        
    default:
        $url = 'index.php';
        $msg = 'Sesión cerrada con éxito';
        $getToPost = "../services/getToPost.php?url=$url&msg=$msg";
        header("Location: $getToPost");    
        exit;            
        break;
}
