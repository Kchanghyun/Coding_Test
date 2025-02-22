-- 코드를 입력하세요
WITH RECURSIVE CTE
AS (
    SELECT 0 AS PRICE_GROUP
    UNION ALL
    SELECT PRICE_GROUP + 10000 
    FROM CTE
    WHERE PRICE_GROUP < (SELECT MAX(PRICE) FROM PRODUCT)
)
SELECT 
    c.PRICE_GROUP,
    COUNT(p.PRODUCT_ID) AS PRODUCTS
FROM CTE c
JOIN PRODUCT p ON p.PRICE >= c.PRICE_GROUP AND p.PRICE < c.PRICE_GROUP + 10000
GROUP BY c.PRICE_GROUP
ORDER BY c.PRICE_GROUP ASC;