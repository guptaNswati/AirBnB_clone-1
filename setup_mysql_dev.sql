-- prepares a MySQL server for storing objects
-- creates the database if not exists
-- creates user and access permissions
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@localhost;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@localhost;
