SELECT DR_NAME,DR_ID,MCDP_CD,date_format(HIRE_YMD,"%Y-%m-%d") as HIRE_YMD
from doctor 
where MCDP_CD="CS" or MCDP_CD="GS"
order by date_format(HIRE_YMD,"%Y-%m-%d") desc, DR_NAME;

'''
조건이 여러개일때 and나 or을 사용할 수 있다.
'''