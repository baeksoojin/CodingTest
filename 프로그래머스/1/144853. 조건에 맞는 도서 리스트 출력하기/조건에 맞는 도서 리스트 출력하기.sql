-- 코드를 입력하세요

SELECT b.BOOK_ID, date_format(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK as b
where b.PUBLISHED_DATE like "2021%" and b.CATEGORY = "인문"
order by PUBLISHED_DATE;