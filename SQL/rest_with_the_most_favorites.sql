-- programmers sql
-- find the restaurant with the most favorites by food type

SELECT FOOD_TYPE, REST_ID, REST_NAME, MAX(FAVORITES)
FROM REST_INFO
WHERE FAVORITES IN (SELECT MAX(FAVORITES)
                  FROM REST_INFO
                  GROUP BY FOOD_TYPE)
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC

-- use SubQuery to find max value from each groups
-- from each rows, find max value from rest_info grouped by food_type
