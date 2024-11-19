<?php
	require_once('services/secureViewAdmin.php');
	$user = getUser();
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>
<a href="managers/loginManager.php">Crear usuario</a><br>
<a href="managers/loginManager.php">Modificar usuario</a><br>
<a href="managers/loginManager.php">Borrar usuario</a><br>
<a href="managers/loginManager.php">Cerrar sesión</a><br>
<br>
<?php
	print_r($user);
	include('view/messages.php');
	getMessage();
?>	
</body>
</html>