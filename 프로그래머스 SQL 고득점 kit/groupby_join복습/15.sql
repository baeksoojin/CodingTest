'''
저자별 카테고리별 매출액 집게


'''

select A.AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(S.SALES * B.PRICE ) as TOTAL_SALES
from BOOK as B
join AUTHOR as A on B.AUTHOR_ID = A.AUTHOR_ID
join BOOK_SALES as S on B.BOOK_ID = S.BOOK_ID
where date_format(S.SALES_DATE,"%Y-%m") = "2022-01"
group by AUTHOR_ID, CATEGORY
order by AUTHOR_ID, CATEGORY desc;
