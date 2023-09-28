-- programmers sql
-- find fruit based icecream

SELECT HALF.FLAVOR -- same result if it is INFO.FLAVOR
FROM FIRST_HALF AS HALF
INNER JOIN ICECREAM_INFO AS INFO
ON HALF.FLAVOR = INFO.FLAVOR
WHERE HALF.TOTAL_ORDER > 3000
AND INFO.INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC

-- using SubQuery
SELECT FLAVOR
FROM FIRST_HALF
WHERE TOTAL_ORDER > 3000
AND FLAVOR IN (SELECT FLAVOR FROM ICECREAM_INFO
              WHERE INGREDIENT_TYPE = 'fruit_based')
ORDER BY TOTAL_ORDER DESC
-- no FLAVOR = (SubQuery)
-- SubQuery returns more than 1 row
-- IN operator returns TRUE if the operand is equal to one of a list of expressions
