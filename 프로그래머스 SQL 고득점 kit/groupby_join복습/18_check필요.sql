'''
그룹별 조건에 맞는 식당 목록 출력하기


ranking을 count값으로 설정

rank over(order by cnt desc) as ranking => 보통 desc를 사용해주는 경우가 많음 ranking은 많을 수록 1위인경우가 현실에서 더 많으니//
.ranking=1 -> 랭킹 1번을 사용.
'''

select M2.MEMBER_NAME, REVIEW_TEXT, date_format(REVIEW_DATE,"%Y-%m-%d") as REVIEW_DATE
from REST_REVIEW as R
join (
    select M1.MEMBER_ID,M1.MEMBER_NAME, rank() over(order by cnt desc) as ranking
    from MEMBER_PROFILE as M1
    join (
        select *, count(REVIEW_ID) as cnt
        from REST_REVIEW
        group by MEMBER_ID
    ) as R1
    on M1.MEMBER_ID = R1.MEMBER_ID
) as M2
on R.MEMBER_ID = M2.MEMBER_ID
where M2.ranking = 1
order by REVIEW_DATE,REVIEW_TEXT


