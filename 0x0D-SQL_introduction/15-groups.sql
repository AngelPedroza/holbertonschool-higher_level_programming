-- list the numbers of records
SELECT
	score, COUNT(*)number
FROM
	second_table
GROUP BY
	score
HAVING
	COUNT(*) > 1
ORDER BY
      score
DESC;
