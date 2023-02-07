SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where (CATEGORY, PRICE) in (select CATEGORY, max(PRICE) as PRICE from FOOD_PRODUCT group by CATEGORY)
and CATEGORY in ("식용유","과자","국","김치")
order by MAX_PRICE desc;

'''

처음에는 그룹안에서 가장 큰 값을 찾아내기 위해서 group by 이후 having으로 조건을 줘야겠다고 생각했는데 작성해보니 having은 그룹끼리의 비교이기 때문에 당연히 틀렸겠다고 생각했다.
그래서 where절을 이용해야했고 그룹별로 max값을 어떻게 뽑아내야하나 생각해보니 select에서 max만 뽑아내면 되는 거였고 이를 subquery로 가져가면 된다고 생각했다.ADD

서브쿼리에서 max값을 뽑아서 사용하면 되는데 어떻게 나오나 한번 출력해봤다.

만약에

# test : max값 뽑기
SELECT CATEGORY, max(PRICE) AS MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
group by CATEGORY
order by MAX_PRICE desc;

해당 코드를 돌리면 어떻게 될까?

CATEGORY	MAX_PRICE	PRODUCT_NAME
김치	19000	맛있는배추김치
식용유	8950	맛있는콩기름
소스	7950	맛있는케첩
...
으로 나올 것이다. 해당 결과를 이용해서 category와 max_price가 같을 경우, 그리고 category가 주어진 조건안에 있울 경우를 고려해 작성하면 될 것이다.


'''