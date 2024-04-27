-- 코드를 입력하세요
SELECT b.author_id, author_name, category, sum(s.sales * b.price) as total_sales
from book as b
inner join author as a on b.author_id = a.author_id
inner join book_sales as s on b.book_id = s.book_id
where date_format(sales_date, "%Y-%m") = "2022-01"
group by author_id, category
order by author_id, category desc;
