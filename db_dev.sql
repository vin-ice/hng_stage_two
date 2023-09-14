-- db setup
CREATE DATABASE IF NOT EXISTS hng_dev_db;
CREATE USER IF NOT EXISTS "hng_dev_user"@"localhost" IDENTIFIED BY "hng_dev_pwd";
GRANT ALL PRIVILEGES ON `hng_dev_db`.* TO "hng_dev_user"@"localhost";
FLUSH PRIVILEGES;
USE 'hng_dev_db';
CREATE TABLE IF NOT EXISTS users (id int NOT NULL AUTO_INCREMENT, 
                                  user_id varchar(40) NOT NULL,
                                  name varchar(128) NOT NULL,
                                  value varchar(128), PRIMARY KEY (id), UNIQUE(user_id));

