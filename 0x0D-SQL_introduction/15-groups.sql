-- Lists the number of records with the same score in second_table
-- Records are ordered by descending count
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY number DESC;
