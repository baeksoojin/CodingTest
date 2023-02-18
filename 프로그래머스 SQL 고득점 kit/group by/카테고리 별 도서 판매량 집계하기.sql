SELECT CATEGORY, sum(SALES) as TOTAL_SALES
from BOOK
inner join BOOK_SALES on BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
where date_format(SALES_DATE,"%Y-%m") = "2022-01"
group by CATEGORY
order by CATEGORY;