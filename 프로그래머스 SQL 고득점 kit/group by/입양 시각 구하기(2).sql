SET @hour := -1;

SELECT (@hour := @hour + 1) as HOUR , 
(select COUNT(*) from ANIMAL_OUTS where HOUR(DATETIME)=@hour) as COUNT
from ANIMAL_OUTS
where @hour<23
order by HOUR;


'''
# SELECT HOUR(DATETIME) as HOUR, COUNT(ANIMAL_ID) as COUNT
# from ANIMAL_OUTS
# group by HOUR(DATETIME)
# order by HOUR;

위의 결과가 틀린 이뉴는 0부터 23시까지 모두 출력하라고 되어있는데 0시부터 23시중 데이터가 없다면 count를 0으로 해서 출력해야함.
따라서 set을 사용해서 @와 함께 변수를 만들고 1을 증가시키면서 0부터 23까지 @hour 담기도록하면서 출력해줘야함

<핵심개념>

set과 @를 통한 쿼리문에서의 로컬 변수를 활용하는 문제
@hour처럼 사용해야하고 초기화를 위해서 = 이 아니라 := 를 사용한다.

'''