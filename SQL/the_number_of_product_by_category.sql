-- programmers sql
-- find the number of product by category (first two char of PRODUCT CODE)

SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(PRODUCT_CODE) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY

-- LEFT(PRODUCT_CODE, 2) to find first two char of PRODUCT_CODE
-- use RIGHT() to find the char from right
