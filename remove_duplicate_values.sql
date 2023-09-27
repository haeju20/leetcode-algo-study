-- programmers sql
-- remove duplicate values

SELECT COUNT(DISTINCT NAME) AS count
FROM ANIMAL_INS
-- WHERE NAME IS NOT NULL

-- the result is same with or without WHERE clause
-- null is not counted in COUNT operator
