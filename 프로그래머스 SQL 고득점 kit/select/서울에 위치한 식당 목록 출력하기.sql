SELECT REST_INFO.REST_ID, REST_INFO.REST_NAME, REST_INFO.FOOD_TYPE, REST_INFO.FAVORITES, REST_INFO.ADDRESS, Round(AVG(REST_REVIEW.REVIEW_SCORE),2) as SCORE
from REST_INFO, REST_REVIEW
where REST_INFO.REST_ID = REST_REVIEW.REST_ID
group by REST_REVIEW.REST_ID
having REST_INFO.ADDRESS like '서울%'
order by SCORE desc, FAVORITES desc;

'''

같은 식당id를 가지는것끼리 join을 해줘야하는데 inner join을 사용하지 않고 동등조인의 경우 where절만 사용해서 조인을 할 수 있다.ADD

from REST_INF join REST_REVIEW on REST_INFO.REST_ID = REST_REVIEW.REST_ID처럼
"from 절에 사용하는 join on 구문을 where절로 동등조건일 때 편하게 where만 사용해도된다."


'''