'''
식품분류별 가장 비싼 식품의 정보 조회하기

식품 종류로 groupby -> max값을 구하면 됨

다시풀기 -> 여태까지 where로 비교한 컬럼만 빼와서 다른 테이블이 만들어지는줄 알았는데 그게 아니라 where를 통해 in으로 비교하고 비교값이 해당 컬럼들인것일뿐 선택되는 것은 그 조건을 만족하는 "행"에 해당하는 (모든 컬럼들)임
=> 그렇기때문에 PRODUCT_NAME을 select 문에서 사용이 가능함
'''

select CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where (CATEGORY, PRICE) in (
    select CATEGORY, max(PRICE) as PRICE
    from FOOD_PRODUCT 
    group by CATEGORY having CATEGORY in ('과자', '국', '김치', '식용유')    )
order by MAX_PRICE desc;
