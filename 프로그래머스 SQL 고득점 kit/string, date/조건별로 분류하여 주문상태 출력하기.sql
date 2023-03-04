SELECT 
    order_id, 
    product_id, 
    date_format(out_date,"%Y-%m-%d") as OUT_DATE	, 
    if(out_date <= '2022-05-01', '출고완료',if(out_date is null, '출고미정','출고대기')) as 출고여부
from food_order
order by order_id