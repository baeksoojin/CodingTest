'''
성분으로 구분한 아이스크림 총 주문량
'''

select I.INGREDIENT_TYPE, sum(TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF as F
join ICECREAM_INFO as I on F.FLAVOR = I.FLAVOR
group by I.INGREDIENT_TYPE
order by TOTAL_ORDER