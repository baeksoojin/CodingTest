SELECT H.CAR_ID, round(avg(timestampdiff(day,H.start_date,H.end_date)) +1,1) as AVERAGE_DURATION
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as H
group by car_id 
having avg(timestampdiff(day,H.start_date,H.end_date) +1) >=7
order by AVERAGE_DURATION desc, CAR_ID desc