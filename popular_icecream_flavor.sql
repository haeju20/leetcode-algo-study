-- programmers sql
-- print the top 3 flavors

SELECT FLAVOR
FROM (SELECT * FROM FIRST_HALF
      UNION
      SELECT * FROM JULY) AS U
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC LIMIT 3

-- use UNION without duplicate data
-- SubQuery needs its own alias
