<?php

function encrypt($string) {
// Creación de una función llamada encrypt.
    $key = "claveSecreta";
    // Establece un valor para la variable $key.
    return base64_encode(openssl_encrypt($string,"AES-128-ECB",$key));
    // Encripta los valores y luego se codifican.
}

function decrypt($string) {
// Creación de una función llamada decrypt.
    $key = "claveSecreta";
    $string = base64_decode($string);
    $decrypt = openssl_decrypt($string,"AES-128-ECB",$key);
	$data = explode('&', $decrypt);
	$data[0] = '../'.$data[0];
	$data[1] = substr($data[1],4);
	return $data;
}

function goToURL($url='index.php', $msg=false) {
/* 
Creación de una función llamada goToURL, la cual se le introducen dos variables que en caso 
de no tener nada dentro, sus valores pasan a ser lo que hay detras de su respectivo igual.
*/
    $encrypted = encrypt("$url&msg=$msg");
    $getToPost = "../services/getToPost.php?p=$encrypted";
    header("Location: $getToPost");    
    exit;
}

function getUser() {
// Creación de una función llamada getUser.
    session_start();
    return array('user' => $_SESSION['user'],'name' => $_SESSION['name'],'type' => $_SESSION['type']);    
}
?>