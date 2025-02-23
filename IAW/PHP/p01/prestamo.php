<?php
	print_r($_REQUEST);


	$capital = $_POST['capital'];
	// plazo <- 15*12;
	$plazo = $_POST['plazo']*12;
	// interes <- (4/100)/12
	$interes = $_POST['interes']/1200;

	$cuota = ($capital*$interes)/(1-pow(1+$interes,-$plazo));
	echo "Importe: $capital<br>";
	echo "Plazo: $plazo<br>";
	echo "Interes: $interes<br>";
	echo "La cuota resultante es de: ".$cuota;


?>