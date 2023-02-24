'''
있었는데요 없었습니다

보호 시작일보다 입양일이 더 빠른 이름을 조회
'''

select I.ANIMAL_ID, I.NAME
from ANIMAL_INS as I
join ANIMAL_OUTS as O on I.ANIMAL_ID = O.ANIMAL_ID
where I.DATETIME > O.DATETIME
order by I.DATETIME