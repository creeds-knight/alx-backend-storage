-- Task 10
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
RETURN IF(b <> 0, a / b, 0);