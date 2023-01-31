SELECT BOOK_ID, date_format(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
from book 
where YEAR(PUBLISHED_DATE) = '2021' and CATEGORY = '인문' 
order by PUBLISHED_DATE asc;