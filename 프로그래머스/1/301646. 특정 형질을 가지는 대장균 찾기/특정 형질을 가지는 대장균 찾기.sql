-- 코드를 작성해주세요
-- 0010 & x = 0010 -> 2번 형질 가지고 있는 경우
-- 0101 & x = 0100 | 0101 & x = 0001 -> 1번 또는 3번 형질 가지고 있는 경우
# SELECT COUNT(*) as COUNT
# FROM ECOLI_DATA
# WHERE (CONV(GENOTYPE, 10, 2) & 0010) != 0010 
# and ((CONV(GENOTYPE, 10, 2) & 0101 = 0100) | (CONV(GENOTYPE, 10, 2) & 0101 = 0001) | (CONV(GENOTYPE, 10, 2) & 0101 = 0101))

SELECT COUNT(*) as COUNT
FROM ECOLI_DATA
WHERE GENOTYPE & 2 != 2
and GENOTYPE & 5 IN (1, 4, 5)