-- Creates a trigger effect that decreases quantity of an itmem after adding a new order
DELIMITER $$
CREATE TRIGGER update_items
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE diff INT;
    DECLARE old_quantity INT;
    SELECT quantity FROM items WHERE name = NEW.item_name INTO old_quantity;
    SET diff = old_quantity - NEW.number;
    UPDATE items
    SET quantity = diff
    WHERE name = NEW.item_name;
END$$
DELIMITER ;
