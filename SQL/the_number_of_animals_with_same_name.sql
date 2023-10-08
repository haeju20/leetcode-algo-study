-- programmers sql
-- count the number of animals with the same name

SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME

-- wrong answer
SELECT NAME, COUNT(ANIMAL_ID) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(ANIMAL_ID) >= 2
ORDER BY NAME

-- column NAME is nullable
-- count the column NAME 
-- or add 'AND NAME IS NOT NULL' to WHERE/HAVING clause
-- to remove the cases when the NAME is NULL
