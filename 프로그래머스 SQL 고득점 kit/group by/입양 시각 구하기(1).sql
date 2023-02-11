SELECT HOUR(DATETIME) as HOUR, COUNT(ANIMAL_ID) as COUNT
from ANIMAL_OUTS
group by HOUR
having HOUR<20 and HOUR>=09
order by HOUR;

'''
시간만 사용하기 위해서는 hour를 사용해서 시간추출이 가능하다.

처음에는 data_format으로 %h로 했는데 %H로 해야한다.
%H, %i, %s => 시간, 분, 초를 가져오는 방법.
연,월,일을 구할 때 %Y, %m, %d인것처럼 첫번째만 대문자라고 기억해두면 편하다!!

이왕알아보는 김에 현재시간을 구하는 방법을 알아보면, date_format(now(), '%H,%i,%s')이다.

'''