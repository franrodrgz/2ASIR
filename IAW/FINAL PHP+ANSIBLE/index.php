<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
	<script type="text/javascript" src="js/jquery-3.7.1.min.js"></script>
	<link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    />
	<link rel="stylesheet" href="style.css" />
</head>
<body>
	<h1>Selección de servicios</h1>
	<form action="exec.php" method="post">
		<div class="wrapper">
			<div class="container">
				<input type="checkbox" id="lamp" name="lamp" value="lamp">
				<label for="lamp"> LAMP</label><br>
				<img src="dessert-01.png" />
			</div>
			<div class="container">		
				<input type="checkbox" id="wp" name="wp" value="wp">
				<label for="wp"> WordPress</label><br>
				<img src="img/wp.png" />
			</div>
			<div class="container">		
				<input type="checkbox" id="md" name="md" value="md">
				<label for="md"> Moodle</label><br>
				<img src="img/md.png" />
			</div>
			<div class="container">		
				<input type="checkbox" id="nc" name="nc" value="nc">
				<label for="nc"> NextCloud</label><br>
				<img src="img/nc.png" />
			</div>
		</div>
		<br>
		<div id="dLamp" style="display: none;" >
			<input type="text" name="lampDomain" placeholder="Nombre de dominio del servidor">
			<input type="password" name="lampMysqlRootPass" placeholder="Contraseña root de MySQL">
		</div>
		<br>
		<div id="dFtp" style="display: none;" >
			<input type="text" name="ftpUser" placeholder="Nombre de usuario FTP">
			<input type="password" name="ftpPass" placeholder="Contraseña del usuario FTP">
		</div>
		<br>
		<div id="dWp" style="display: none;" >
			<input type="text" name="wpDomain" placeholder="Nombre de dominio WordPress">
		</div>
		<br>
		<div id="dMd" style="display: none;" >
			<input type="text" name="mdDomain" placeholder="Nombre de dominio Moodle">
		</div>
		<div id="dNc" style="display: none;" >
			<input type="text" name="mdDomain" placeholder="Nombre de dominio NextCloud">
		</div>	
		<input type="submit" value="Instalar servicios">
	</form>
	<script type="text/javascript">
		$(document).ready(function() {
			$("#lamp").click(function() {
				if($(this).is(":checked")) {		
		        	$('#dLamp').show();
		        	$('#dFtp').show();
    			} else {
		        	$('#dLamp').hide();
		        	$('#dFtp').hide();    				
    			}
			});			
		});

		$(document).ready(function() {
			$("#md").click(function() {
				if($(this).is(":checked")) {		
		        	$('#dMd').show();
		        	$('#dFtp').show();
    			} else {
		        	$('#dMd').hide();
		        	$('#dFtp').hide();			
    			}
			});			
		});

		$(document).ready(function() {
			$("#wp").click(function() {
				if($(this).is(":checked")) {		
		        	$('#dWp').show();
		        	$('#dFtp').show();
    			} else {
		        	$('#dWp').hide();
		        	$('#dFtp').hide();  				
    			}
			});			
		});

		$(document).ready(function() {
			$("#nc").click(function() {
				if($(this).is(":checked")) {		
		        	$('#dNc').show();
		        	$('#dFtp').show();
    			} else {
		        	$('#dNc').hide();
		        	$('#dFtp').hide();  				
    			}
			});			
		});
	</script>
</body>
</html>