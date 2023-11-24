-- programmers sql
-- print the information of places owned by heavy users

SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID FROM PLACES
      GROUP BY HOST_ID
      HAVING COUNT(ID) >= 2)
ORDER BY ID

-- use WHERE to find host id, not id
-- to know all id owned by same one host
