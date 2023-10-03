-- programmers sql
-- find the list of sales by author, and category

SELECT USER_ID, NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_USER AS U
ON B.WRITER_ID = U.USER_ID
AND STATUS = 'DONE'
GROUP BY WRITER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES

-- HAVING: condition of GROUP BY clause
-- after GROUP BY clause
-- WHERE cannot be used with aggregate func. (SUM, COUNT, ...)
