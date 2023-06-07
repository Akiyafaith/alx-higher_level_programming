-- list all cities found in the db
-- sort results in asc order

SELECT * FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
