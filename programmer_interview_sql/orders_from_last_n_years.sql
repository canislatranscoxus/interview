/*
Get the orders from the last 23 years.
With this idea we can do in the last 30 days, in the last 2 months...

The strategy is real simple:

    * the N years range has a starting point in time P1, and finish point P2 that is today. 
    * we find the stating point in time P1.
    * we filter to get rows that are in our range using a WHERE clause. 
      We can use any of both options:
        + WHERE order_date >= P1
        + WHERE P1 <= order_date 


*/
use sales;

select o.cust_id ,o.order_date , date_sub( CURRENT_DATE(), interval 23 year )  last_23_years
from Orders o
where  date_sub( current_date(), interval 23 year ) <= o.order_date ;

/* select o.cust_id ,o.order_date 
	, year( from_days(to_days( current_date() ) - to_days( o.order_date) ) )    last_years
from Orders o; */

/*select o.cust_id ,o.order_date ,  from_days( datediff( CURRENT_DATE(), o.order_date ) )
,extract( year from
	from_days( datediff( CURRENT_DATE(), o.order_date ) )
) 
from Orders o
where  extract( year from
	from_days( datediff( CURRENT_DATE(), o.order_date ) )
) <= 23 
;*/

#SELECT CURRENT_DATE(), EXTRACT(YEAR FROM CURRENT_DATE() );
#select CURRENT_DATE, current_time, current_timestamp, EXTRACT( YEAR FROM CURRENT_DATE() );
