-- Use a sub query
-- just do it
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id=states.id AND states.name="California"
ORDER BY cities.id ASC;
