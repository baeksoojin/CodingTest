-- 2021년에 가입한 회원중 구매한 사람들을 찾기 위해서 join -> 중복제거를 위해서 distinck

select YEAR,MONTH, count(U.USER_ID) as PUCHASED_USERS, 
ROUND((COUNT(*)/ (SELECT COUNT(*) FROM USER_INFO WHERE YEAR(JOINED) = 2021)), 1) AS PUCHASED_RATIO
from (select distinct YEAR(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, I.USER_ID
        from USER_INFO as I 
        join ONLINE_SALE as O on I.USER_ID = O.USER_ID and YEAR(JOINED) = 2021) as U
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH