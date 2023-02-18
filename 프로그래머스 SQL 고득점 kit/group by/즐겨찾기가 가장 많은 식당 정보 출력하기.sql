select FOOD_TYPE,REST_ID,REST_NAME,FAVORITES
from REST_INFO
where (FOOD_TYPE,FAVORITES) in (select FOOD_TYPE, MAX(FAVORITES) as FAVORITES from REST_INFO group by FOOD_TYPE)
order by FOOD_TYPE desc;

'''
처음에 틀렸던 이유 : group by를 적용하면 select할 때 뽑는 값이 해당 기준으로 grouping된 것의 대표값이 뽑히는는데 rest_id값이 즐겨찾기가 max일때라는것을 보장하지 않음
그러나, subquery에서 REST_ID를 뽑아내도록 해서 틀림. FOOD_TYPE을 뽑아내거나 REST_ID를 뽑아내려고 했다면 where절에서 MAX(FAVORITES)의 id값을 뽑아내도록 조건을 줬어야함.
where (REST_ID,FAVORITES) in (select REST_ID, MAX(FAVORITES) as FAVORITES from REST_INFO group by FOOD_TYPE)

=> where (FOOD_TYPE,FAVORITES) in (select FOOD_TYPE, MAX(FAVORITES) as FAVORITES from REST_INFO group by FOOD_TYPE)

'''