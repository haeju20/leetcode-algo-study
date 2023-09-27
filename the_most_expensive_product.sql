-- programmers sql
-- print the information of the most expensive product

-- using LIMIT 1
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1

-- using SubQuery
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)
