-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(date_of_birth, '%Y-%m-%d') as DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE DATE_FORMAT(date_of_birth, '%m') = '03' and GENDER = 'W' and TLNO is not NULL
ORDER BY member_id ASC;