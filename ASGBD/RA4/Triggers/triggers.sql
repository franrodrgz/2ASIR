delimeter ::
CREATE TRIGGER newImporte
BEFORE INSERT
ON lineapedidos FOR EACH ROW
BEGIN
  IF NEW.precioventa < 0 THEN
    set NEW.precioventa = 0;
   END IF;
END::
delimiter ;
