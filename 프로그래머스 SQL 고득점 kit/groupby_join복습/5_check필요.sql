'''
입양시각 구하기(2)

입양이 가장 활발하게 일어났는지 0시부터 23시까지

데이터가 존재하지 않더라도 group을 만들어서 출력해야함
범위가 지정해져있으니까 시간을 담을 변수를 set @hour:=-1을 통해서 만들고 +1씩 증가시키면서 해당 변수를 사용하고 @hour가 22까지(+1하면 23까지니까)돌기

'''

set @hour := -1;

select (@hour := @hour+1) as HOUR, (select count(*) from ANIMAL_OUTS where HOUR(DATETIME)=@hour) as COUNT
from ANIMAL_OUTS
where @hour<23

