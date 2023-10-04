-- programmers sql
-- find the total numbers of rental per month by car_id during 2022-08 ~ 2022-10

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(HISTORY_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (SELECT CAR_ID
               FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
               WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
               GROUP BY CAR_ID
               HAVING COUNT(HISTORY_ID) >= 5)
AND START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
-- set time period again
-- to find the records during the specific period
GROUP BY MONTH(START_DATE), CAR_ID
-- group by month and by car_id
HAVING COUNT(HISTORY_ID) != 0
-- exclude the record if the total numbers of rental in a particular month
ORDER BY MONTH(START_DATE), CAR_ID DESC
