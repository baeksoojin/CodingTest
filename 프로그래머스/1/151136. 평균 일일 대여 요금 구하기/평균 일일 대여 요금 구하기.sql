# select * from CAR_RENTAL_COMPANY_CAR as c where  CAR_TYPE = "SUV";

select round(avg(c.DAILY_FEE),0) as AVERAGE_FEE from CAR_RENTAL_COMPANY_CAR as c where CAR_TYPE = "SUV";