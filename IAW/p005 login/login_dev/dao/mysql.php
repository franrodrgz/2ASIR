<?php
function getLink() {
// Creación de una función llamada getLink.
	try {
	    $link = mysqli_connect("127.0.0.1", "prestamosdbuser", "prestamosdbuser", "prestamosdb");
		// Variable que contiene la conexión a la Base de Datos, con su IP, usuario, contraseña, y base de datos que vas a seleccionar.
	} catch (Exception $e) {
	    header('Location: getToPost.php?url=index.php&msg=Se ha detectado una incidencia temporal en el servicio de datos');
		// En caso de incidencia o de que la conexión no se produzca correctamente, manda un mensaje de error atraves de la cabecera.    
	    exit;
	}
	return $link;
}

?>