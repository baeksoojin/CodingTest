select F.FLAVOR
from (select F.FLAVOR, rank() over(order by TOTAL_ORDER_J+TOTAL_ORDER desc) as ranking
from (select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER_J
from JULY
group by FLAVOR) as J
join FIRST_HALF as F on F.FLAVOR = J.FLAVOR) as R
join FIRST_HALF as F on R.FLAVOR = F.FLAVOR
where ranking <4