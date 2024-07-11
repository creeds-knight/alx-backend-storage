-- Creates a table while leveraging the use of enum to create a column with specific
-- entries

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(
	id INTEGER NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM('US', 'CO', 'TN') DEFAULT 'US',
	PRIMARY KEY(id)
);
