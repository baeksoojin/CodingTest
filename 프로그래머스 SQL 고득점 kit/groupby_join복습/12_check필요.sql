'''
자동차 대여 기록에서 대여중/대여가능 여부 구분하기

retry 필요
가장 최근에 빌렸던 내용중에서 대여중인지 아닌지 체크해야하니까 max를 사용해야함
'''

select CAR_ID, if(max("2022-10-16" between date_format(START_DATE,"%Y-%m-%d") and date_format(END_DATE,"%Y-%m-%d")),'대여중',"대여 가능") as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
order by CAR_ID desc;