'''
5월 식품들의 총매출 조회하기
'''


select P.PRODUCT_ID,P.PRODUCT_NAME, sum(O.AMOUNT*P.PRICE) as TOTAL_SALES
from FOOD_PRODUCT as P
join FOOD_ORDER as O on P.PRODUCT_ID = O.PRODUCT_ID
where date_format(PRODUCE_DATE,"%Y-%m") = "2022-05"
group by P.PRODUCT_ID
order by TOTAL_SALES desc, P.PRODUCT_ID