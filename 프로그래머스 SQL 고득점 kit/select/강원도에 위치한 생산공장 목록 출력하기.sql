SELECT FACTORY_ID,FACTORY_NAME,ADDRESS 
from FOOD_FACTORY
where ADDRESS like '강원도%'
order by FACTORY_ID;


'''
like와 %(와일드카드)를 사용해서 문자열에서 특정 글자를 포함하는 행을 필터링 할 수 있다.
'''