-- Use a sub query
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id=states.id AND states.id="California"
ORDER BY cities.id;
