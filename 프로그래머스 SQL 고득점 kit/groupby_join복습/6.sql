'''
가격대별 상품 개수 구하기

가격대로 나누고 상품 개수를 count집계함수 이용해서 구하기
'''

select floor(PRICE/10000)*10000 as PRICE_GROUP, count(PRODUCT_ID) as PRODUCTS
from PRODUCT
group by PRICE_GROUP
order by PRICE_GROUP