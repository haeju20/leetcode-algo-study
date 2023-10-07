-- programmers sql
-- print the list of availability of car rent from rental records

SELECT CAR_ID, IF (CAR_ID IN (SELECT CAR_ID
                             FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                             WHERE START_DATE <= '2022-10-16'
                             AND END_DATE >= '2022-10-16'), '대여중', '대여 가능')
                             AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC

-- use CASE WHEN / IF to return different values based on condition
-- CASE WHEN CAR_ID IN (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
-- WHERE START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16')
-- THEN '대여중' ELSE '대여 가능' END AVAILABILITY
-- use IN because there are duplicate car_id values in history table
