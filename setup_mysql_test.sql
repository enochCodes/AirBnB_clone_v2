-- A SCRIPT TO PREPARE THE SERVER FOR THE PROJECT (TESTING)--
-- CREATE DATABASE `hbnb_test_db` --
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- MAKE THE DATABASE ACTIVE --
USE hbnb_test_db;
-- CREATE USER `hbnb_test` WITH A PASSWORD `hbnb_test_pwd` --
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- GRANT SELECT ON `performance_schema` TO `hbnb_test` --
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
