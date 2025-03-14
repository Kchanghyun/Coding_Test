-- 코드를 입력하세요
# SELECT DATE_FORMAT(START_DATE, '%c') AS MONTH, CAR_ID, COUNT(*) AS RECORDS
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
# GROUP BY CAR_ID, MONTH
# HAVING COUNT(*) >= 5
# ORDER BY MONTH ASC, CAR_ID DESC

# SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE MONTH(START_DATE) BETWEEN 8 AND 10
# GROUP BY MONTH(START_DATE), CAR_ID
# HAVING COUNT(*) >= 5
# ORDER BY MONTH ASC, CAR_ID DESC;

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (
    SELECT CAR_ID 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE MONTH(START_DATE) BETWEEN 8 AND 10
    GROUP BY CAR_ID
    HAVING COUNT(*) >= 5
) 
AND MONTH(START_DATE) BETWEEN 8 AND 10
GROUP BY MONTH(START_DATE), CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC;