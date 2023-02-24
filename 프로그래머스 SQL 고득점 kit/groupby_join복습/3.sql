'''
동명 동물 수 찾기

우선이름이 두번이상 쓰인것을 select해야함
이름이 같은 것의 횟수를 조회해야함 -> 이름으로 group by 해야함

'''

select NAME, count(ANIMAL_ID) as COUNT
from ANIMAL_INS
group by NAME having count(NAME)>=2
order by NAME
