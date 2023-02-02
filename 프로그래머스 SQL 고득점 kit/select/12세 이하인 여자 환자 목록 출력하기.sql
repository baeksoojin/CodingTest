SELECT PT_NAME, PT_NO, GEND_CD,AGE, If(TLNO is null, "NONE", TLNO) as TLNO 
from PATIENT 
where AGE<=12 and GEND_CD = "W" 
order by AGE desc, PT_NAME;

'''
select 문장에 조건문을 넣을 수 있는데 if(조건문, 참일때 실행, 거짓일때 실행)

null 값을 체크하려면 "is null"을 사용한다.
'''
