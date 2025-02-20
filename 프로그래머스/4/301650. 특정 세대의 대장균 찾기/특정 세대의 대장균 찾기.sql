-- 코드를 작성해주세요
SELECT f.ID
FROM ECOLI_DATA f
JOIN ECOLI_DATA s ON f.PARENT_ID = s.ID
JOIN ECOLI_DATA t ON s.PARENT_ID = t.ID
WHERE t.PARENT_ID is NULL
ORDER BY f.ID ASC;