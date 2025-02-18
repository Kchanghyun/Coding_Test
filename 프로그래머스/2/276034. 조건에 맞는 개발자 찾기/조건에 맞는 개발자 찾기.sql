-- 코드를 작성해주세요
-- SKILLCODES 이름, 범주, 코드
-- DEVELOPERS ID, 이름, 성, 이메일, 코드
SELECT distinct(d.ID), d.EMAIL, d.FIRST_NAME, d.LAST_NAME
FROM DEVELOPERS d
JOIN SKILLCODES s ON d.SKILL_CODE & s.CODE
WHERE s.Name = 'Python' or s.Name = 'C#'
ORDER BY ID ASC;