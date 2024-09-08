-- Task 12
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE weighted_avg FLOAT;
    SELECT DISTINCT
        SUM(c.score * p.weight) / SUM(p.weight) INTO weighted_avg
    FROM
        corrections AS c
    LEFT JOIN projects AS p
    ON p.id = c.project_id
    WHERE
        c.user_id = user_id;

    UPDATE users
    SET average_score = weighted_avg
    WHERE id = user_id;

END $$
DELIMITER ;
