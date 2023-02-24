'''
대여횟수가 많은 자동차들의 월별 대여 횟수 구하기

차 아이디를 가지고 group by 하고 우선 대여 횟수가 8월붙 10월까지 5회이상인지 체크해야함
월별로 나눠줘야해서 group by를 사용해야하함

다시풀어보기!!

'''

select MONTH(START_DATE) as MONTH, CAR_ID, count(HISTORY_ID) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date_format(START_DATE,"%Y-%m") between "2022-08" and "2022-10"
    group by CAR_ID having count(HISTORY_ID)>=5
) and date_format(START_DATE,"%Y-%m") between "2022-08" and "2022-10"
group by MONTH, CAR_ID
order by MONTH, CAR_ID desc;
