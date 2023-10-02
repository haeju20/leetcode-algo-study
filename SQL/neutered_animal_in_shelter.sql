-- programmers sql
-- find animals that were not neutered when they entered the shelter
-- but were neutered when they left the shelter

SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_INS AS INS
JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE LIKE 'Intact%'
AND (OUTS.SEX_UPON_OUTCOME LIKE 'Spayed%'
     OR OUTS.SEX_UPON_OUTCOME LIKE 'Neutered%')
-- AND OUTS.SEX_UPON_OUTCOME REGEXP ('Spayed|Neutered')
-- can use NOT LIKE 'Intact%' to exclude 'Spayed%' and 'Neutered%'
ORDER BY INS.ANIMAL_ID

-- results of INNER JOIN / LEFT OUTER JOIN / RIGHT OUTER JOIN are all same
-- SEX_UPON_INTAKE / SEX_UPON_OUTCOME column is duplicated in both tables
-- and check only SEX_UPON_INTAKE / SEX_UPON_OUTCOME column from both tables
