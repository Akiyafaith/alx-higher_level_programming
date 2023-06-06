-- A script that creates a user
-- grant the user all privileges and set password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
SELECT USER  FROM mysql.user WHERE User = 'user_0d_1' AND Host = 'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
