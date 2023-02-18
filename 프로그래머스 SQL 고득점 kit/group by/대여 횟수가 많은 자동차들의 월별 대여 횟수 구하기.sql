SELECT  MONTH(START_DATE) as MONTH,  CAR_ID, COUNT(CAR_ID) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in (select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY where DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10' group by CAR_ID having count(CAR_ID)>=5) and DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
group by MONTH,CAR_ID
having RECORDS<>0
order by MONTH, CAR_ID desc;

'''
CAR_ID를 8~10월까지 5회 이상인 것을 먼저 구하지 않고 having에서 조건을 줘버리면 group에서 5번 이상인 것들만 가져와서 month별로 나눠진 상태에서 5회이상인 것을 가져오게 됨.
따라서 car_id를 먼저 구하고 해당 car_id만 사용하는 것으로 where문의 조건을 주면 되게 한다.
여기서도 착각각해서 안의 조건에 8~10월의 조건 적용했으니 안 하는 경우가 있을 수도 있는데, id값이 그 사이의 횟수가 5회 이상이라고 해도 해당 id값을 활용할 때 조건의 달이 아닌 다른 월이라고 해도 그 id가 포함될 수 있기에 조건을 걸어줘야함

그리고 월의 대여 횟수가 0인 것은 group화를 month별로 그룹화했을 때 id값이 1개도 없다면 0이니까 그룹화한 후에 해당 그룹에 조건을 걸 수 있으니 having을 적용

'''