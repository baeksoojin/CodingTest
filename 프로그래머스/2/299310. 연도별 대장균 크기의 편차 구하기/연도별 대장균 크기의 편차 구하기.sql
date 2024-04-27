-- 코드를 작성해주세요

# WITH MAXS AS (
# SELECT MAX(SIZE_OF_COLONY) AS MAXSIZE
# , YEAR(DIFFERENTIATIONDATE) AS YEAR
# FROM ECOLIDATA
# GROUP BY YEAR )

# select YEAR(DIFFERENTIATION_DATE) as YEAR, a.size_of_colony-b.max_size as YEAR_DEV, a.id
# from ECOLI_DATA a
# left join (
#     select id, max(size_of_colony) as max_size, YEAR(DIFFERENTIATION_DATE) AS YEAR
#     from ECOLI_DATA
#     group by YEAR
# ) as b on a.id = b.id

SELECT YEAR(a.DIFFERENTIATION_DATE) AS YEAR,
       MAX(a.size_of_colony) OVER (PARTITION BY YEAR(a.DIFFERENTIATION_DATE))- a.size_of_colony  AS YEAR_DEV,
       a.id
FROM ECOLI_DATA a
order by year, year_dev;