-- 자동차 대여 기록 별 대여 금액 구하기
SELECT P.HISTORY_ID,ROUND((DAILY_FEE * (100 - IFNULL(DISCOUNT_RATE, 0)) /100) * PERIOD) AS FEE
from (SELECT 
       C.CAR_ID,C.CAR_TYPE,C.DAILY_FEE, H.HISTORY_ID, TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 AS PERIOD,
    CASE 
        WHEN 
            TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 90 THEN '90일 이상'
        WHEN 
            TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 30 THEN '30일 이상'
        WHEN 
            TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 7 THEN '7일 이상'
        ELSE 
            '7일 미만' 
    END AS DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as H
    join CAR_RENTAL_COMPANY_CAR as C on H.CAR_ID = C.CAR_ID) as P
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as D on D.CAR_TYPE = P.CAR_TYPE and P.DURATION_TYPE = D.DURATION_TYPE
where P.CAR_TYPE like '%트럭%'
order by FEE desc, HISTORY_ID desc;


'''
날짜 차이구하기
timestampdiff(주기,start,end )+1 -> 경과한 요일

<주기>
SECOND : 초
MINUTE : 분
HOUR : 시
DAY : 일
WEEK : 주
MONTH : 월
QUARTER : 분기
YEAR : 연

TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 AS PERIOD

timestampdiff(기준, start, end)에다가 "+1"을 해줘야 period가 됨


'''