-- create a table first_table
-- with description id and name if the table exists it should not fail
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
)
