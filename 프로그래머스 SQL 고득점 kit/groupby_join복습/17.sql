'''
조건에 맞는 도서와 저자 리스트 출력하기
'''

select BOOK_ID, AUTHOR_NAME, 
date_format(PUBLISHED_DATE,"%Y-%m-%d") as PUBLISHED_DATE
from BOOK
join AUTHOR on BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
where CATEGORY like "%경제%"
order by PUBLISHED_DATE