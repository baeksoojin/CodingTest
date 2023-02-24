'''
고양이와 개는 몇 마리 있을까
고양이와 개는 각각 몇마리인지 조회하고 고양이를 개보다 먼저 조회
c -> d
'''

select ANIMAL_TYPE, count(ANIMAL_ID) as count
from ANIMAL_INS
group by ANIMAL_TYPE
having ANIMAL_TYPE in ("Cat", "Dog")
order by ANIMAL_TYPE