-- 코드를 입력하세요
SELECT count(*)
FROM USER_INFO
WHERE DATE_FORMAT(JOINED, '%Y') = '2021' and AGE <= 29 and AGE >= 20;