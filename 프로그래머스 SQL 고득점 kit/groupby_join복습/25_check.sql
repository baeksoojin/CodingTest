'''
상품을 구매한 회원 비율 구하기

'''



SELECT DATE_FORMAT(ONLINE.sales_date, '%Y') YEAR,
       DATE_FORMAT(ONLINE.sales_date, '%m') MONTH,
       COUNT(DISTINCT ONLINE.user_id) PUCHASED_USERS,
       round(COUNT(DISTINCT ONLINE.user_id) 
             / (SELECT COUNT(user_id)
                FROM user_info
                WHERE DATE_FORMAT(joined, '%Y') = '2021'), 1) PUCHASED_RATIO
FROM user_info USERINFO JOIN online_sale ONLINE
     on (USERINFO.user_id = ONLINE.user_id) 
WHERE DATE_FORMAT(USERINFO.joined, '%Y') = '2021'
GROUP BY YEAR, MONTH