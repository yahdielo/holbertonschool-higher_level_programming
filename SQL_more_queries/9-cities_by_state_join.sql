-- list all cities in databse
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN state ON cities.state_id = states.id;