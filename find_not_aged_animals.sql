-- programmers sql
-- find the 'not aged' animals

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NOT INTAKE_CONDITION = 'Aged'
-- INTAKE_CONDITION != 'Aged'
-- no 'IS NOT' (used with 'IS NOT NULL')
ORDER BY ANIMAL_ID
