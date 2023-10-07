-- programmers sql
-- print how many adoptions occurred in each time period from 0:00 to 23:00

WITH RECURSIVE RE AS(
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR + 1 FROM RE
    WHERE HOUR < 23
)

SELECT RE.HOUR AS HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM RE
LEFT JOIN ANIMAL_OUTS AS OUTS
ON RE.HOUR = HOUR(OUTS.DATETIME)
GROUP BY HOUR
ORDER BY HOUR

-- use RECURSIVE to make time period column HOUR
