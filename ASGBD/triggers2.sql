-- EJERCICIO 3

DELIMITER ::

CREATE TRIGGER stock
AFTER INSERT 
ON lineapedido FOR EACH ROW
BEGIN 
    -- Declarar una variable la cual usaremos para guardar la cantidad de stock de productos que hay
    DECLARE stock_actual INT;

    -- Obtener el stock actual del producto
    SELECT enAlmacen INTO stock_actual
    FROM productos
    WHERE codProducto = NEW.codProducto;

    -- Verificar si hay suficiente stock
    IF NEW.cantidad > stock_actual THEN
    -- En caso de no haberlo manda un mensaje de error
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No hay suficiente stock para este producto';
    ELSE
        -- Si hay suficiente stock, actualizar el inventario, cuando el codigo de producto coincidan
        UPDATE productos
        SET enAlmacen = enAlmacen - NEW.cantidad
        WHERE codProducto = NEW.codProducto;
    END IF;
END::

DELIMITER ;
