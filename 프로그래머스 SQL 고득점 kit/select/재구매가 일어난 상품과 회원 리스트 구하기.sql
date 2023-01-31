-- 코드를 입력하세요

# SELECT USER_ID, PRODUCT_ID 
# from ONLINE_SALE 
# group by PRODUCT_ID having count(USER_ID)>=2
# order by USER_ID, PRODUCT_ID desc;

'''
위의 코드는 틀렸습니다.가 나옴

PRODUCT_ID만으로 그룹화를 하면 '3'인 PRODUCT_ID를 가지는 user가 달라도 같은 그룹이여서 having절에서 user마다 재구매를 한건지를 알 수가 없게 됨.
group_by는 묶은 것을 한번에 같은 그룹으로 생각해서 where절에서의 행처럼 변경하는 것이라고 보면됨.
group_by의 경우, where절은 하나의 행만 관여해서 having을 사용해야함.

'''

SELECT USER_ID, PRODUCT_ID 
from ONLINE_SALE 
group by PRODUCT_ID,USER_ID having count(*)>=2
order by USER_ID, PRODUCT_ID desc;


