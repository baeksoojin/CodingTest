SELECT ANIMAL_TYPE, Count(*) as count
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE;