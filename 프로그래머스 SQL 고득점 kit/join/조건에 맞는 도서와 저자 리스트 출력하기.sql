SELECT BOOK_ID, AUTHOR_NAME, date_format(PUBLISHED_DATE,"%Y-%m-%d") as PUBLISHED_DATE
from book
inner join author on book.AUTHOR_ID = author.AUTHOR_ID
where book.CATEGORY = "경제"
order by PUBLISHED_DATE;

'''

author의 id값이 동일한 것을 찾아서 book에 author name을 집어 넣어주는 inner join이다.
사실 inner join 대신 join을 사용해도 되고 where문을 사용해서 where book.AUTHOR_ID = author.AUTHOR_ID라고 적어도 성립한다.

[sql 구문 익히기]

=> from [atable(결과를 저장할 테이블)] join [btable] on [조건]
=> 양쪽 테이블에 있는 내용을 모두 사용할 때 inner join을 사용한다.


'''