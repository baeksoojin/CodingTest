select F.FLAVOR
from (select F.FLAVOR, rank() over(order by TOTAL_ORDER_J+TOTAL_ORDER desc) as ranking
from (select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER_J
from JULY
group by FLAVOR) as J
join FIRST_HALF as F on F.FLAVOR = J.FLAVOR) as R
join FIRST_HALF as F on R.FLAVOR = F.FLAVOR
where ranking <4

'''
subquery 활용 ranking제한걸기
'''

-- 다른 코드도 살펴보니 flavor를 중복제거해서 구한다음(inner join /left join 혹은 right join) 해서 다른 id여도 같은 flavor가 여러개 있어도 고려되도록함

SELECT A.FLAVOR
FROM FIRST_HALF A 
left JOIN JULY B ON B.FLAVOR = A.FLAVOR
GROUP BY A.FLAVOR
ORDER BY SUM(A.TOTAL_ORDER) + SUM(B.TOTAL_ORDER) DESC
LIMIT 3