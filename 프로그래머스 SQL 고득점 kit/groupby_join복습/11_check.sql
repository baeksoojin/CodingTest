'''
즐겨찾기가 가장 많은 식당 정보 출력하기

주의) group by 를 food_type으로 했으면 그 그룹안에서 rest_id는 having이 하나로 만들어주지 않는다면, 아무거나 뽑힘. -> 정렬한 것을 기준으로 분류해야해서
rest_id를 select해서 in으로 비교하는 것이 아닌 정렬기준인 food_type으로 비교해야함

'''

-- 틀린코드
-- select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
-- from REST_INFO
-- where (REST_ID,FAVORITES ) in ( 
--     select REST_ID, max(FAVORITES) as FAVORITES
--     from REST_INFO
--     group by FOOD_TYPE 
-- )
-- order by FOOD_TYPE desc;

-- 수정 후 

select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from REST_INFO
where (FOOD_TYPE,FAVORITES ) in ( 
    select FOOD_TYPE, max(FAVORITES) as FAVORITES
    from REST_INFO
    group by FOOD_TYPE 
)
order by FOOD_TYPE desc;

