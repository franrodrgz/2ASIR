<?php
	require_once('services/secureView.php');
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
<form action="start.php" method="post">
		<input type="number" name="capital" placeholder="Importe préstamo" required>
		<input type="number" name="interes" placeholder="Interés anual" required>
		<input type="number" name="plazo" placeholder="Años del préstamo" required>
		<select name="periodicidad">
			<option value="1">Anual</option>
			<option value="2">Semestral</option>
			<option value="4">Trimestral</option>
			<option value="6">Bimensual</option>
			<option value="12">Mensual</option>
		</select>
		<input type="submit" value="Enviar">		
	</form>
	<?php
	$pr = $_REQUEST['periodicidad'];
	$c = $_REQUEST['capital'];
	$i = $_REQUEST['interes']/(100*$pr);
	$n = $_REQUEST['plazo']*$pr;
	$cuota = ($c*$i)/(1-pow(1+$i,-$n));

	$p = $c;	// pendiente igual a capital inicial
	$tc = $n+1;	// total cuotas igual al numero de cuotas + 1 (para el bucle)
	$ic = 0;	// interes cuota
	$ac = 0;	// amortizacion cuota
	echo 'Cuota: '.number_format($cuota, 2, '.', '')."<br>\n";
	for($x=1;$x<$tc;$x++) {
		$ic = $i*$p;
		$ac = $cuota - $ic;
		$p = $p - $ac;
		echo "$x\t$ic\t$ac\t$p<br>\n";
	}

?>
<a href="managers/loginManager.php">Cerrar sesión</a><br>
<br>
<?php
	include('view/messages.php');
	getMessage();
?>	
</body>
</html>