-- Task 13
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
        JOIN (
            SELECT DISTINCT
                c.user_id AS user_id,
                SUM(c.score * p.weight) as total_score,
                SUM(p.weight) as total_weight
            FROM
                corrections AS c
            LEFT JOIN projects AS p ON p.id = c.project_id
            GROUP BY c.user_id
        ) AS sq ON users.id = sq.user_id
    SET users.average_score = sq.total_score / sq.total_weight;
END $$
DELIMITER ;
