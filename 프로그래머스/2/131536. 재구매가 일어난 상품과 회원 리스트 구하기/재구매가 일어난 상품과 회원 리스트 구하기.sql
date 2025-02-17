-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID 
FROM ONLINE_SALE
GROUP BY user_id, product_id
HAVING count(*) > 1
ORDER BY user_id ASC, product_id DESC;