<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
	<script type="text/javascript" src="js/jquery-3.7.1.min.js"></script>
</head>
<body>
	<form action="<?php echo $_SERVER['PHP_SELF']; ?> " method="post">
 		<label for="unftp">Número de usuarios de FTP</label><br>
		<select name="unftp" id="unftp"  style="min-width: 100px;">
			<option selected="selected" value="0">0</option>
			<option value="1">1</option>
			<option value="2">2</option>
		</select>		
	</form>
	<form action="exec.php" method="post">
		<div style="display: none;" id="div1ftpu">
			<input type="text" name="user[]" placeholder="Usuario1">
			<input type="password" name="pass[]" placeholder="Contraseña1">
		</div>
		<div style="display: none;" id="div2ftpu">
			<input type="text" name="user[]" placeholder="Usuario2">
			<input type="password" name="pass[]" placeholder="Contraseña2">
		</div>
		<input type="submit" id="btnFTP" value="VsFTP" disabled>		
	</form>
</body>
<script type="text/javascript">
	$(function() {
	    $('#unftp').change(function(){
	        $('#div1ftpu').hide();
	        $('#div2ftpu').hide();
			var n = $('#unftp').find(":selected").text();
			switch(n) {
			  case '1':
		        $('#div1ftpu').show();
				$("#btnFTP").prop('disabled', false);		        		        
			    break;
			  case '2':
		        $('#div1ftpu').show();
		        $('#div2ftpu').show();
				$("#btnFTP").prop('disabled', false);		        
			    break;
			  default:
		        $('#div1ftpu').hide();
		        $('#div2ftpu').hide();
				$('#btnFTP').prop('disabled', true);		        
			} 				    	
	    });
	});	
</script>
</html>