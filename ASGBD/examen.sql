/* EXAMEN SQL FRANCISCO JOSÉ RODRÍGUEZ MUÑOZ */

/* EJERCICIO 1 */
/* Crea un procedimiento que incrementa el precio de un producto en el porcentaje especificado. Tanto el codigo del producto como el porcentaje a incrementar se pasaran al procedimiento como parametros. */
/* FRANCISCO JOSÉ RODRÍGUEZ MUÑOZ */

DELIMITER //

CREATE PROCEDURE incPrecio(IN codigoIN INT,IN porcentaje INT)
BEGIN
DECLARE precioInicial INT;
DECLARE precioFinal double;
DECLARE precioMedio double;
     	SELECT producto.precio INTO precioInicial
     	FROM producto
     	WHERE producto.codigo = codigoIN;
     	SET precioMedio = (precioInicial * porcentaje)/100;
     	SET precioFinal = precioMedio+precioInicial;
     	SELECT precioFinal;
	UPDATE producto SET producto.precio = precioFinal WHERE producto.codigo = codigoIN;
     	
END //

DELIMITER ;

/* EJERCICIO 2 */
/* Crea una funcion que devuelva TRUE o FALSE si un producto tiene un precio superior a 500€. La funcion debe recibir el codigo de producto. */
/* FRANCISCO JOSÉ RODRÍGUEZ MUÑOZ */

DELIMITER //

CREATE FUNCTION precioSup(codigoIN INT)
RETURNS VARCHAR(255)
DETERMINISTIC
  BEGIN
	DECLARE s VARCHAR(255);
	DECLARE precioT INT;
     	SELECT producto.precio INTO precioT
     	FROM producto
     	WHERE producto.codigo = codigoIN;
     	
     	IF precioT > 500 THEN
           SET s = 'TRUE';
     	ELSE
           SET s = 'FALSE';
        END IF;    
        RETURN s;
END //

DELIMITER ;

/* EJERCICIO 3 */
/* Crea un disparador que haga la comprobacion al insertar un nuevo producto y si no puede insertarlo muestre el mensaje "Error" */

/* FRANCISCO JOSÉ RODRÍGUEZ MUÑOZ */
DELIMITER //

CREATE TRIGGER productosMaxPrueba
BEFORE INSERT ON producto
  FOR EACH ROW
  BEGIN
  DECLARE conteo INT;
       SELECT count(producto.codigo_fabricante) INTO conteo
       FROM producto
       GROUP BY producto.codigo_fabricante;

       IF conteo > 100 THEN
           SIGNAL SQLSTATE '45000'
       SET MESSAGE_TEXT = 'ERROR. Ese fabricante ya suministra 100 productos.';
       END IF;
END //
DELIMITER ;
