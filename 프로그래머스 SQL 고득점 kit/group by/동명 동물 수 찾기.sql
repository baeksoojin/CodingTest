SELECT NAME, COUNT(NAME) as COUNT
from ANIMAL_INS
group by NAME having Count(NAME) >= 2
order by NAME;