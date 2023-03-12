-- list all cities in databse
SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states ON cities.state_id = states.id
OEDER BY cities.id ASC;