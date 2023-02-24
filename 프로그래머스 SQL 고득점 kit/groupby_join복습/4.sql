'''
입양시각 구하기(1)

시간별로 입양 건수를 구해야하는 문제
다만, 9시부터 19:59까지니까 시간이 9시부터 19사이에 있는지 where
이때 어차피 그룹의 조건이 시간이니까 having을 사용해도 무관함.
'''

select HOUR(DATETIME) as HOUR, COUNT(ANIMAL_ID) as COUNT
from ANIMAL_OUTS
where HOUR(DATETIME) between 09 and 19
group by HOUR(DATETIME)
order by HOUR