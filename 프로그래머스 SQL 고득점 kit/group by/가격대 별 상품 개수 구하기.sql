
SELECT truncate(PRICE,-4) as PRICE_GROUP, count(PRODUCT_ID) as PRODUCTS
from PRODUCT
group by PRICE_GROUP
order by PRICE_GROUP;


-- SELECT TRUNCATE(3456.1234567 ,1) FROM DUAL;
-- // 3456.1
 
-- SELECT TRUNCATE(3456.1234567 ,4) FROM DUAL;
-- // 3456.1234
 
-- SELECT TRUNCATE(3456.1234567 ,-1) FROM DUAL;
-- // 3450
 
-- SELECT TRUNCATE(3456.1234567 ,-2) FROM DUAL;
-- // 3400 
