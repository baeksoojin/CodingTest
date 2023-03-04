SELECT ANIMAL_ID, NAME
from ANIMAL_INS
where NAME like "%EL%" and ANIMAL_TYPE="Dog"
order by NAME