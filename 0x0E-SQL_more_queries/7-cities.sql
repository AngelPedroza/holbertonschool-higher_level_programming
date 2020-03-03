-- Another try
-- Add another comment  to prouve
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT UNIQUE AUTO_INCREMENT NOT NULL DEFAULT 1,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       CONSTRAINT cities_ibfk_1 FOREIGN KEY (state_id) REFERENCES states(id)
);
