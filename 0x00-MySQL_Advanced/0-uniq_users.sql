-- script creates table users
CREATE TABLE IF NOT EXISTS users
(
	id INT NOT NULL,
	email VARCHAR(255) UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY(id)
);
