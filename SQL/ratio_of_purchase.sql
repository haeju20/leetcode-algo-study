-- programmers sql
-- find the ratio of members who purchased a product by year / month
-- (members who joined in 2021 and purchased a product / members who joined in 2021)

SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) MONTH,
COUNT(DISTINCT SALE.USER_ID) AS PUCHASED_USERS,
ROUND(COUNT(DISTINCT SALE.USER_ID) / (SELECT COUNT(USER_ID)
                            FROM USER_INFO
                            WHERE JOINED
                            LIKE '2021%'), 1)
                            AS PUCHASED_RATIO
FROM ONLINE_SALE AS SALE
JOIN USER_INFO AS INFO
ON SALE.USER_ID = INFO.USER_ID
AND JOINED LIKE '2021%'
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE)
ORDER BY YEAR(SALES_DATE), MONTH(SALES_DATE)

-- use DISTINCT when count the numbers of members to remove the duplicate user_id
