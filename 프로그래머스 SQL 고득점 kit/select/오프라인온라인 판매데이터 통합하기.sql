-- 두개의 테이블을 합집합을 사용해서 조건에 맞춰서 select

select date_format(SALES_DATE, "%Y-%m-%d") as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from ONLINE_SALE
where date_format(SALES_DATE, "%Y-%m") = '2022-03'

union

select date_format(SALES_DATE, "%Y-%m-%d") as SALES_DATE, PRODUCT_ID, Null as USER_ID, SALES_AMOUNT
from OFFLINE_SALE
where date_format(SALES_DATE, "%Y-%m") = '2022-03'

order by SALES_DATE, PRODUCT_ID, USER_ID

'''
각 table마다 설정한 select문이 존재한다면?
두개의 select query문을 합치고 싶을 때 union을 사용

union all은 중복을 제거하지 않고 union은 중복을 제거
다만 여기서는 중복을 신경쓰지 않아도 되니까 그냥 UNION

'''