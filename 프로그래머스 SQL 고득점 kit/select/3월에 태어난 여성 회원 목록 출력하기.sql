SELECT MEMBER_ID,MEMBER_NAME,GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH 
from MEMBER_PROFILE 
where month(DATE_OF_BIRTH) = '3' and GENDER = 'W' and TLNO is not NULL 
order by MEMBER_ID;

'''
구문 select ~ from ~ where ~ ordery by ~;

DATE의 경우 %Y-%d-%m를 사용해서 "시간"을 제외하고 날짜만 선택이 가능하다.
=> date_format을 사용. 
=> date_format(column, '%Y-%m-%d')

이때 m은 month 숫자이고 M은 달의 명칭(Month 등)으로 string이다
이때 d는 숫자이고 D는 English suffix를 붙인(0th, 1st, 2nd, 3rd) 이다

만약 시간만 뽑고 싶다면??

===>> date_format(column, '%h:%i:%s') 를 사용한다

'''