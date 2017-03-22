-- prepares a MySQL server for testing object and storing
-- creates the database if not exists
-- creates user and access permissions
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@localhost;
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@localhost;
