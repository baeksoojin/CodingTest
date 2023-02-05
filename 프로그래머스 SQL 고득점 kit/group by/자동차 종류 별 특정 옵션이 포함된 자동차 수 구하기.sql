SELECT CAR_TYPE, count(CAR_TYPE) as CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS like '%통풍시트%' or  OPTIONS like '%열선시트%' or OPTIONS like '%가죽시트%'
group by CAR_TYPE
order by CAR_TYPE;