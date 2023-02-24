'''
9시 50분 시작
진료과별 총 예약 횟수 출력하기
'''

select MCDP_CD as '진료과 코드', count(PT_NO) as '5월예약건수'
from APPOINTMENT
where date_format(APNT_YMD,"%Y-%m") = "2022-05"
group by MCDP_CD
order by count(PT_NO),MCDP_CD