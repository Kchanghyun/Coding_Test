-- 코드를 작성해주세요
SELECT l.ID, COUNT(r.PARENT_ID) as CHILD_COUNT
FROM ECOLI_DATA l
LEFT JOIN ECOLI_DATA r ON l.ID = r.PARENT_ID
GROUP BY l.ID
ORDER BY l.ID ASC;