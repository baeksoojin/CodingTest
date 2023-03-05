'''
특정 기간동안 대여 가능한 자동차들의 대여비용 구하기

다시체크
'''

-- 우선 대여가능한 차의 목록을 뽑아내기

select C.CAR_ID, C.CAR_TYPE, Round(C.DAILY_FEE*30*(100-D.DISCOUNT_RATE)/100) as FEE
from CAR_RENTAL_COMPANY_CAR as C
join CAR_RENTAL_COMPANY_RENTAL_HISTORY as R on C.CAR_ID = R.CAR_ID
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as D on  C.CAR_TYPE = D.CAR_TYPE 
where C.CAR_ID not in (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where END_DATE >= '2022-11-01' AND START_DATE <= '2022-12-01'
) and  D.DURATION_TYPE like "%30일 이상%"
group by C.CAR_ID 
having C.CAR_TYPE in ("SUV","세단") and (FEE>=500000 AND FEE<2000000)
order by FEE DESC, CAR_TYPE, CAR_ID DESC

