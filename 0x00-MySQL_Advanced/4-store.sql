-- Creates a trigger effect that decreases quantity of an itmem after adding a new order

DROP TRIGGER IF EXISTS reduce_qnty;
DELIMETER //
CREATE TRIGGER reduce_qnty
AFTER INSERT ON orders
FOR EACH ROW
	BEGIN
		UPDATE items
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
	END //
DELIMETER ;
