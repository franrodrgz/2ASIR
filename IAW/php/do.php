<?php
$n1 = $_REQUEST['n1'];
$n2 = $_REQUEST['n2'];

function menorMayor($a, $b) {
	$resultado = array($a, $b);
	if($b<$a) $resultado = array($b,$a);
	return $resultado;
}

// 2.5 puntos
// Debe mostrar en pantalla si el dividendo es divisible por el divisor
// Ejemplo: 2 es divisible por 10
function divisible($dividendo, $divisor) {
	$array = menorMayor($dividendo, $divisor);
	$divisor = $array[1];
	$dividendo = $array[0];
	if ($dividendo%$divisor) print("$dividendo es divisible por $divisor <br>\n");
}

// 2.5 puntos
// Debe mostrar en pantalla la relación mayor, menor o igual entre los números
// Condición: hacer uso if anidados
// Ejemplo: 2 es menor que 10
function compara($a, $b) {
	$resultado = "";
	if ($a>$b) {
		print("$a es mayor que $b");
	} elseif ($a<$b) {
		print("$a es menor que $b");
	} else {
		print("$a y $b son iguales");
	}
	echo "$resultado<br>\n";

}

// 2.5 puntos
// Debe mostrar en pantalla todos los números del número más pequeño hasta el más grande
// Condición: hacer uso de bucle for
// Ejemplo: 2 3 4 5 6 7 8 9 10
function listado($inf,$sup) {
	$array = menorMayor($inf, $sup);
	$final = $array[1];
	$sup = $array[0];
	$i=1;
	for ($i=$inf; $i<=$final; $i++ ) {
		$resultado = $i;
		print("$resultado ");
		if (esPrimo($i)) echo "es primo ab <br>\n";
		else echo "no es primiyo xico ab <br>\n";
	}
	print("<br>");
}
function esPrimo($i) {
	$x = 2;
	for ($x; $x<$i; $x++) {
		if ($i%$x == 0) return false;
	}
	return true;
}

// 2.5 puntos
// Debe mostrar en pantalla del número menor elevado al mayor
// Condición: hacer uso de bucle while
// Ejemplo: 2 elevado a 10 es 1024
function potencia($base, $exp) {
	$contador = 1;
	$resultado2 = 1;
	while ($contador<=$exp) {
		$resultado2*=$base;
		$contador++;
	}
	print("$base elevado a $exp es $resultado2<br>\n");
}
divisible($n1,$n2);
compara($n1,$n2);
listado($n1,$n2);
potencia($n1,$n2);
listadoFactorial($n1,$n2);

// 2.5 puntos
// Debe mostrar en pantalla el factorial de un número
function listadoFactorial($inf,$sup) {
	$array = menorMayor($inf, $sup);
	$final = $array[1];
	$sup = $array[0];
	for ($i=$inf; $i<=$final; $i++ ) {
		print(factorial($i)."<br>\n");
	}
}

function factorial($num) {
	$i = 1;
	$resultado = 1;
	for ($i; $i<=$num; $i++) {
		$resultado*=$i;
	}
	return "El factorial de $num es $resultado";
}

?>