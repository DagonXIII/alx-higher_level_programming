-- Print full table description
SELECT TABLE_NAME AS "Table", CREATE_TABLE AS "Create Table"
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
