-- programmers sql
-- find three animals that have been in the shelter the longest

SELECT INS.NAME, INS.DATETIME
FROM ANIMAL_INS AS INS
LEFT JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.DATETIME IS NULL
ORDER BY INS.DATETIME LIMIT 3

-- use LEFT JOIN to get all of the data in left table(INS)
-- and based on that data, see if data in right table(OUTS) is null
