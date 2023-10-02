-- programmers sql
-- find the lost record

SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_INS AS INS
RIGHT JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
ORDER BY OUTS.ANIMAL_ID

-- use RIGHT JOIN to remain NULL data of ANIMAL_INS