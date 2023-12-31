-- programmers sql
-- find the rental fee of cars available for a specific period of time

SELECT CAR.CAR_ID, CAR.CAR_TYPE, ROUND((CAR.DAILY_FEE * 30) * (100 - DIS.DISCOUNT_RATE)/100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS CAR

JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS DIS
ON CAR.CAR_TYPE = DIS.CAR_TYPE
AND DIS.DURATION_TYPE = '30일 이상'
AND CAR.CAR_TYPE IN ('세단','SUV')

LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS HIS
ON CAR.CAR_ID = HIS.CAR_ID
AND HIS.END_DATE >= '2022-11-01' AND HIS.START_DATE <= '2022-11-30'
WHERE ((CAR.DAILY_FEE * 30) * (100 - DIS.DISCOUNT_RATE)/100) BETWEEN 500000 AND 1999999
AND HIS.CAR_ID IS NULL

ORDER BY FEE DESC, CAR.CAR_TYPE, CAR.CAR_ID DESC

-- first use INNER JOIN with DIS to find discount rate
-- use AND after JOIN/ON to limit the range of the data (based on duration type AND car type)
-- then use LEFT OUTER JOIN with HIS to combine the rental history for each cars
-- set the range of HIS.END_DATE AND HIS.START_DATE that span the rental period (11/1~11/30)
-- if the data is not in the range, it will be NULL because of LEFT OUTER JOIN
