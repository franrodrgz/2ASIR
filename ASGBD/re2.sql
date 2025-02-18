/* RELACIÓN DE EJERCICIOS 2. AUTOMATIZACIÓN DE TAREAS */

/* EJERCICIO 1 */
/* Crea un procedimiento que modifique la tabla pedidos para añadirle un atributo llamado “importe”. Debe darle el valor de la suma de los importes de las lineas de pedido que le correspondan. */

DELIMITER //  -- Corrección: "DELIMITER" estaba mal escrito
CREATE PROCEDURE sumaImporte()
BEGIN  -- El bloque BEGIN debe estar al inicio del procedimiento
    -- Verificar si la columna 'importe' existe
    IF NOT EXISTS (
        SELECT 1 
        FROM information_schema.columns 
        WHERE 
            TABLE_SCHEMA = DATABASE() AND
            TABLE_NAME = 'pedidos' AND 
            COLUMN_NAME = 'importe'
    ) THEN
        ALTER TABLE pedidos ADD COLUMN importe INT;
    END IF;

    -- Actualizar el importe usando JOIN explícito
    UPDATE pedidos p
    INNER JOIN (
        SELECT 
            numeroPedido, 
            SUM(precio) AS precioTotal  -- Suma los precios por pedido
        FROM lineapedido
        GROUP BY numeroPedido  -- Agrupa por el número de pedido
    ) lp ON p.numeroPedido = lp.numeroPedido  -- Relación entre tablas
    SET p.importe = lp.precioTotal;  -- Asignación correcta
END //
DELIMITER ;

/* EJERCICIO 2 */
/* Escribe un procedimiento que diga si hay o no pedidos cancelados. */

DELIMITER //
CREATE PROCEDURE pedidosCancelados()
BEGIN
        SELECT *
        FROM pedidos
        WHERE estado='cancelado';
END //
DELIMITER ;

/* EJERCICIO 3 */
/* Crea un procedimiento que muestre cuantos pedidos se han hecho en una fecha que recibe como parámetro. Si no existe ninguno debe mostrar “No hay pedidos en esa fecha”. */

DELIMITER //
CREATE PROCEDURE fechaPedidos(IN fecha DATE)
BEGIN
DECLARE contador INT;
DECLARE mensaje VARCHAR(255);
        SELECT COUNT(*) INTO contador
        FROM pedidos
        WHERE pedidos.fechaPedido = fecha;
        
        IF contador > 0 THEN
           SET mensaje = 'Hay pedidos en esa fecha';
        ELSE
           SET mensaje = 'No hay pedidos en esa fecha';
        END IF;
        
        SELECT mensaje AS resultado;
END //
DELIMITER ;

/* EJERCICIO 4 */
/* Crea un procedimiento que recibe como parámetro un año y cuenta los pedidos de ese año. Después mostrará devolverá en un parámetro de salida los siguientes mensajes según corresponda: */
/* “Menos de 100 pedidos” */
/* “Entre 100 y 150 pedidos” */
/* “Más de 150 pedidos” */

DELIMITER //
CREATE PROCEDURE fechaPedidos2(IN fecha DATE)
BEGIN
    DECLARE contador INT;
    DECLARE mensaje VARCHAR(255);
    
    SELECT COUNT(*) INTO contador
    FROM pedidos
    WHERE pedidos.fechaPedido = fecha;
    
    IF contador > 150 THEN
        SET mensaje = 'Hay más de 150 pedidos en esa fecha';
    ELSEIF contador > 100 THEN
        SET mensaje = 'Hay más de 100 pedidos en esa fecha';
    ELSE
        SET mensaje = 'Hay 100 o menos pedidos en esa fecha';
    END IF;

    SELECT mensaje AS resultado;
END //
DELIMITER ;

/* EJERCICIO 5 */
/* Crea un procedimiento que recibe el nombre de una categoría y un número. El procedimiento mostrará tantos productos de la categoría como indique el número. Por ejemplo si recibe la categoría “pulseras” y el número 5, mostrará cinco productos de la categoría “pulseras”. El número debe estar entre 1 y 10, de lo contrario no hará nada y mostrará el mensaje “El número no es válido”. */


