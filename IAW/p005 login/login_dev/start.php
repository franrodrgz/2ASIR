<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>
<?php
	include('view/messages.php');
	getMessage();
	require_once('services/basic.php');
	$user = getUser();
?>	
<a href="managers/loginManager.php">Cerrar sesión</a>
</body>
</html>