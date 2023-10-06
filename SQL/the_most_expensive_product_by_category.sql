-- programmers sql
-- print the information of the most expensive product by category

SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE PRICE IN (SELECT MAX(PRICE)
               FROM FOOD_PRODUCT
               GROUP BY CATEGORY)
GROUP BY CATEGORY
HAVING CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY PRICE DESC

-- use WHERE clause to find the most expensive product grouped by CATEGORY
-- then use HAVING to see if the category meets the given condition
