-- programmers sql
-- get a list of the repurchased products and users

SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY USER_ID, PRODUCT_ID DESC

-- for finding duplicate data,
-- group the user_id and product_id
-- count(*) means the numbers of grouped user_id and product_id
