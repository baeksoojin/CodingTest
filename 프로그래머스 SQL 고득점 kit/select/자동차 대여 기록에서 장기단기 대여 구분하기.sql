-- 코드를 입력하세요
SELECT 
HISTORY_ID,
CAR_ID, 
date_format(START_DATE,"%Y-%m-%d") as START_DATE,
date_format(END_DATE,"%Y-%m-%d") as END_DATE,
if(DATEDIFF(END_DATE, START_DATE) < 29 , '단기 대여','장기 대여' ) as RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE LIKE '2022-09-%'
order by HISTORY_ID desc;

'''
30일이 아닌 29일을 기준으로 해주는 것은 당일에도 +1일이기 때문이다.

DATEDIFF를 통해서 date의 차이를 알아낼 수 있다.
DATEDIFF에는 구분자를 넣어줘서 year, day, hour등을 구할 수 있는데
SELECT DATEDIFF(dd,'2018-01-01','2018-12-31') + 1 처럼 사용한다.(결과는 365)

yy, qq(분기),mm,dd,wk,m(시간- hour), mi(분)
'''