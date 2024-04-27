-- 코드를 입력하세요
SELECT p.PT_NAME, p.PT_NO, p.GEND_CD, p.AGE, If(TLNO is null, "NONE", TLNO) as TLNO
from PATIENT as p
where p.GEND_CD = "W" and p.AGE <=12
order by p.age desc, p.PT_NAME;

-- if('조건문', 참일때 값, 거짓일 때 값) -> null일때는 ifnull도 존재함. 그리고 collaesc도 가능