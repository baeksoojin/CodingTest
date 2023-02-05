SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE 
from FOOD_PRODUCT 
order by PRICE desc
limit 1 offset 0;

'''
만약에 max값을 찾아서 비교하고 싶다면 subquery와 Max를 사용하면 된다.

SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE 
from FOOD_PRODUCT 
where PRICE = (select max(PRICE) price from FOOD_PRODUCT);

max일때의 price값을 우선 뽑아내야하니까, subquery를 통해서 price를 찾아낸다.

'''