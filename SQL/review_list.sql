-- programmers sql
-- print the list of reviews from members who have written the most reviews

SELECT PROFILE.MEMBER_NAME, REVIEW.REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS PROFILE
JOIN REST_REVIEW AS REVIEW
ON PROFILE.MEMBER_ID = REVIEW.MEMBER_ID
WHERE PROFILE.MEMBER_ID = (SELECT MEMBER_ID
                         FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                        ORDER BY COUNT(*) DESC
                        LIMIT 1)
ORDER BY REVIEW_DATE, REVIEW_TEXT

-- using SubQuery to find member who have written the most reviews
-- using GROUP BY to group reviews by member_id
