-- A SCRIPT TO PREPARE THE SERVER FOR THE PROJECT --
-- CREATE DATABASE `hbnb_dev_db` --
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- MAKE THE DATABASE ACTIVEi --
USE hbnb_dev_db;
-- CREATE USER `hbnb_dev` WITH A PASSWORD `hbnb_dev_pwd` --
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- GRANT SELECT ON `performance_schema` TO `hbnb_dev` --
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
