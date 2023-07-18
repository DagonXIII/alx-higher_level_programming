-- List all tables in a specific database
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'mysql';
