-- 코드를 작성해주세요
-- 2022년도 평가점수 가장 높은 사원들 점수, 사번, 성명, 직책, 이메일 조회
SELECT SUM(g.SCORE) AS SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
FROM HR_EMPLOYEES e
JOIN HR_GRADE g ON e.EMP_NO = g.EMP_NO
WHERE g.YEAR = 2022
GROUP BY e.EMP_NO
ORDER BY SCORE DESC
LIMIT 1;