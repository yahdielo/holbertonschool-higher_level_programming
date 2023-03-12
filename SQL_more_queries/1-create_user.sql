-- create a new user
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEDGES ON * . * TO USER 'user_0d_1'@'localhost';