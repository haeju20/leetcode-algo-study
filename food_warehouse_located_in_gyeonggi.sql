-- programmers sql
-- print the food warehouses located in Gyeonggi-do

SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N')
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID

-- if there's no freezer, print 'N'
-- COALESCE(FREEZER_YN, 'N')
-- IFNULL is for MySQL
-- COALESCE is for ORACLE/MSSQL/MySQL
