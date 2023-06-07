-- list all cities found in the db
-- sort results in asc order
USE hbtn_0d_usa;

SELECT * FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'California'
)
ORDER BY id ASC;
