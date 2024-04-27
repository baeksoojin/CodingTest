-- 코드를 입력하세요

# select * from USED_GOODS_BOARD where writer_id = "xlqpfh2";

# xlqpfh2
SELECT USER_ID, NICKNAME, (
    concat(city, ' ', STREET_ADDRESS1 , " ", STREET_ADDRESS2)
) AS 전체주소, (
    concat(substring(tlno, 1, 3), "-", substring(tlno, 4,4), "-", substring(tlno,8,4))
) AS 전화번호
from USED_GOODS_USER as u
left join USED_GOODS_BOARD as b on u.user_id = b.writer_id
group by user_id
having count(*) >=3
order by user_id desc;

# SELECT U.USER_ID, U.NICKNAME, 
#     CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ', IFNULL(U.STREET_ADDRESS2, '')) AS 전체주소, 
#     CONCAT(SUBSTRING(U.TLNO, 1, 3), '-', SUBSTRING(U.TLNO, 4, 4), '-', SUBSTRING(U.TLNO, 8)) AS 전화번호
# FROM USED_GOODS_BOARD B JOIN USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID
# GROUP BY U.USER_ID
# HAVING COUNT(U.USER_ID) >= 3
# ORDER BY U.USER_ID DESC;