'''

경기도에 위치한 식품창고 목록 출력하기
'''

select  WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, if(FREEZER_YN is not null,FREEZER_YN, 'N') as FREEZER_YN
from FOOD_WAREHOUSE
where ADDRESS like '%경기%'
order by WAREHOUSE_ID;