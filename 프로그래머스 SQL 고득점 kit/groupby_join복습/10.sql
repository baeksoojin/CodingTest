'''
카테고리별 도서 판매량 집계하기
'''

select B.CATEGORY, sum(SALES) as TOTAL_SALES
from BOOK as B
join BOOK_SALES as S on B.BOOK_ID = S.BOOK_ID
where date_format(SALES_DATE,"%Y-%m") = "2022-01" 
group by B.CATEGORY
order by B.CATEGORY;