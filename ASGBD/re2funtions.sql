/* RELACIÓN DE EJERCICIOS 2. AUTOMATIZACIÓN DE TAREAS */

/* EJERCICIO 2 */
/* Escribe una funcion que diga si hay o no pedidos cancelados. */

DELIMITER //

CREATE FUNCTION PedidosCancelados() 
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    DECLARE total INT;
    SELECT COUNT(*) INTO total 
    FROM pedidos 
    WHERE estado = 'cancelado';
    
    IF total > 0 THEN
        RETURN 'Hay pedidos cancelados';
    ELSE
        RETURN 'No hay pedidos cancelados';
    END IF;
END //

DELIMITER ;

/* EJERCICIO 3 */
/* Crea una funcion que muestre cuantos pedidos se han hecho en una fecha que recibe como parámetro. Si no existe ninguno debe mostrar “No hay pedidos en esa fecha”. */

DELIMITER //

CREATE FUNCTION pedidosFecha(fecha DATE)
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    DECLARE total INT;
    SELECT COUNT(*) INTO total 
    FROM pedidos 
    WHERE pedidos.fechaPedido = fecha;
    
    IF total > 0 THEN
        RETURN 'Hay pedidos en esa fecha';
    ELSE
        RETURN 'No hay pedidos en esa fecha';
    END IF;
END //

DELIMITER ;

/* EJERCICIO 4 */
/* Crea una funcion que recibe como parámetro un año y cuenta los pedidos de ese año. Después mostrará devolverá en un parámetro de salida los siguientes mensajes según corresponda: */
/* “Menos de 100 pedidos” */
/* “Entre 100 y 150 pedidos” */
/* “Más de 150 pedidos” */

DELIMITER //

CREATE FUNCTION pedidosFecha2(fecha DATE)
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    DECLARE total INT;
    SELECT COUNT(*) INTO total 
    FROM pedidos 
    WHERE pedidos.fechaPedido = fecha;
    
    IF total > 150 THEN
        RETURN 'Hay más de 150 pedidos en esa fecha';
    ELSEIF total > 100 THEN
        RETURN 'Hay más de 100 pedidos en esa fecha';
    ELSE
        RETURN 'Hay menos de 100 pedidos en esa fecha';
    END IF;
END //

DELIMITER ;
