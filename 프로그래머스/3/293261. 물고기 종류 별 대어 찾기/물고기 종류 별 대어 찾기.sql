-- 코드를 작성해주세요

# select i.ID, n.fish_name, max(i.length) as LENGTH
# from FISH_INFO as i, FISH_NAME_INFO as n 
# where i.FISH_TYPE = n.FISH_TYPE
# group by i.FISH_TYPE;


# select id, fish_name, length
# from fish_info a inner join fish_name_info b
# on a.fish_type = b.fish_type
# where a.length = (select max(length)
#                  from fish_info
#                  group by fish_type
#                  having id = a.id)
# order by id;

SELECT id, fish_name, length
FROM fish_info a INNER JOIN fish_name_info b
ON a.fish_type = b.fish_type
WHERE (a.fish_type, a.length) IN (
    SELECT fish_type, MAX(length)
    FROM fish_info
    GROUP BY fish_type
)
ORDER BY id;