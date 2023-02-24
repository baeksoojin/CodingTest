'''
보호소에서 중성화한 동물
'''


select I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
from ANIMAL_INS as I
right join (
    select ANIMAL_ID, ANIMAL_TYPE, NAME
    from ANIMAL_OUTS
    where SEX_UPON_OUTCOME like "%Spayed%" or SEX_UPON_OUTCOME like "%Neutered%"
) as O on O.ANIMAL_ID = I.ANIMAL_ID
where I.SEX_UPON_INTAKE like "%Intact%"
order by O.ANIMAL_ID;
