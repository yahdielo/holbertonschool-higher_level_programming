-- create a new table and add new rows
CREATE TABLE IF NOT EXISTS hbtn_0c_0.second_table (`id` int(10), `name` varchar(256), `score` int(10));
INSERT INTO second_table (`id`, `name`, `score`) Values ('1', 'John', '10'), ('2', 'Alex', '3'), ('3', 'Bob', '14'), ('4', 'George', '8'); 