-- Converts the entire database hbtn_0c_0 to UTF8
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
