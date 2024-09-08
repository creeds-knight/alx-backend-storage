-- Task5: Sends out a validation after email is set
DELIMITER $$
CREATE TRIGGER update_state
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email
    THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;
