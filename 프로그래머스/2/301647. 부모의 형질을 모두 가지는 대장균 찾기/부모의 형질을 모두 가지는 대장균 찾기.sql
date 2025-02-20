-- 코드를 작성해주세요
-- 자식 형질 & 부모 형질 = 부모 형질 -> 부모 형질 모두 보유한 대장균
SELECT c.ID, c.GENOTYPE, a.GENOTYPE as PARENT_GENOTYPE
FROM ECOLI_DATA c
JOIN ECOLI_DATA a ON c.PARENT_ID = a.ID
WHERE c.GENOTYPE & a.GENOTYPE = a.GENOTYPE
ORDER BY ID ASC;