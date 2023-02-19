SELECT O.ANIMAL_ID, O.NAME
from ANIMAL_OUTS as O
left join ANIMAL_INS as I on O.ANIMAL_ID = I.ANIMAL_ID
where O.ANIMAL_ID not in (
    select ANIMAL_ID 
    from ANIMAL_INS
)