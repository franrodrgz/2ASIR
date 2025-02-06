DELIMITER $$

CREATE TRIGGER verificar_stock
BEFORE INSERT ON lineapedido
FOR EACH ROW
BEGIN
    DECLARE stock_disponible INT;

    -- Obtener el stock disponible para el producto
    SELECT stock INTO stock_disponible
    FROM productos
    WHERE id_producto = NEW.id_producto;

    -- Verificar si la cantidad solicitada es mayor que el stock
    IF NEW.cantidad > stock_disponible THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No hay suficiente stock para este producto';
    END IF;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER actualizar_importe_pedido
AFTER INSERT ON lineapedido
FOR EACH ROW
BEGIN
    DECLARE nuevo_importe DECIMAL(10, 2);

    -- Calcular el nuevo importe total del pedido
    SELECT SUM(l.cantidad * p.precio)
    INTO nuevo_importe
    FROM lineapedido l
    JOIN productos p ON l.id_producto = p.id_producto
    WHERE l.id_pedido = NEW.id_pedido;

    -- Actualizar el importe del pedido
    UPDATE pedidos
    SET importe = nuevo_importe
    WHERE id_pedido = NEW.id_pedido;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER disminuir_stock_producto
AFTER INSERT ON lineapedido
FOR EACH ROW
BEGIN
    -- Actualizar el stock del producto
    UPDATE productos
    SET stock = stock - NEW.cantidad
    WHERE id_producto = NEW.id_producto;
END$$

DELIMITER ;

