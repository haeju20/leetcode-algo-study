-- programmers sql
-- print the list of restaurants located in Seoul

-- using INNER JOIN
SELECT INFO.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO AS INFO
INNER JOIN REST_REVIEW AS REVIEW
ON INFO.REST_ID = REVIEW.REST_ID
WHERE INFO.ADDRESS LIKE '서울%'
GROUP BY INFO.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC

-- using WHERE
SELECT INFO.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO AS INFO, REST_REVIEW AS REVIEW
WHERE INFO.REST_ID = REVIEW.REST_ID
AND INFO.ADDRESS LIKE '서울%'
GROUP BY INFO.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC

-- use GROUP BY to group the data by rest_id to calculate the average of each restaurant
-- the result of it is average score for "each restaurant", not just one restaurant
