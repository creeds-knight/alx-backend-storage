-- Task6
DELIMITER $$
CREATE PROCEDURE AddBonus(user_id INT, project_name CHAR(255), score FLOAT)
BEGIN
    DECLARE projectid INT DEFAULT 1;
    IF NOT EXISTS(SELECT * FROM projects WHERE name = project_name)
    THEN
        INSERT INTO projects (name)
        VALUES(project_name);
    END IF;

    SELECT id INTO projectid FROM projects WHERE name = project_name;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, projectid, score);
END $$
DELIMITER ;
