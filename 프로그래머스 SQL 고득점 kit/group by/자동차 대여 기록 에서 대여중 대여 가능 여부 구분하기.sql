SELECT CAR_ID, 
if(max('2022-10-16' BETWEEN DATE_FORMAT(START_DATE, '%Y-%m-%d') AND DATE_FORMAT(END_DATE, '%Y-%m-%d')), '대여중','대여 가능') AS AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
order by CAR_ID desc;


'''


알아두기! case when [조건] then [true일때 수행문] else [false일때 수행문] end

SELECT CAR_ID, 
MAX(CASE WHEN '2022-10-16' BETWEEN DATE_FORMAT(START_DATE, '%Y-%m-%d') AND DATE_FORMAT(END_DATE, '%Y-%m-%d')
THEN '대여중' 
ELSE '대여 가능'
END) AS AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
order by CAR_ID desc;


위와같이 작성해도됨 case when [] then [] else [] end


'''