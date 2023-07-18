-- List all records with score >= 10 in the table second_table
-- Ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESCi;
