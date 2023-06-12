--┌───────────────────────────────────────────────────────────────────────────┐
--│ Windows Funtions                   				                          │
--└───────────────────────────────────────────────────────────────────────────┘

-- select payment_id, customer_id, rental_id, amount, payment_date from payment;
--select  * from payment;






/*

-- limiting with RANGE 
select  payment_id, customer_id, rental_id, amount, payment_date ,

	SUM(amount) 
	OVER ( PARTITION BY customer_id ORDER BY  payment_date 
		 RANGE BETWEEN '2 days' PRECEDING AND '2 days' FOLLOWING
		 )
	AS total_2_days
	

from payment;



-- OVER ( PARTITION BY ... ORDER BY ... frame_clause )
-- Limiting the window, with frame_clause
select payment_id, customer_id, rental_id, amount,


		SUM( amount )
		over ( partition by customer_id order by payment_id 
			   ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW )
		as amount_begin_to_here,

		SUM( amount )
		over ( partition by customer_id order by payment_id 
			   ROWS 2 PRECEDING )
		as amount_2_preceding,
		
		SUM( amount )
		over ( partition by customer_id order by payment_id 
			   ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING )
		as amount_2_following,

		SUM( amount )
		over ( partition by customer_id order by payment_id 
			   ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING )
		as amount_all_window

from payment
order by payment_id
;



-- Limiting the window, with FILTER
select payment_id, customer_id, rental_id, amount,

		SUM( amount )
		filter( where amount < 5 )
		over ( partition by customer_id order by payment_id )
		as total_amount

from payment
order by payment_id
;

select  inventory_id, film_id,

		ROW_NUMBER()
		over ( partition by film_id order by inventory_id )
		as row_number

from inventory;



select  n,
		ROW_NUMBER() 	OVER ( ORDER BY n), 
		RANK() 		 	OVER ( ORDER BY n), 
		DENSE_RANK() 	OVER ( ORDER BY n), 
		PERCENT_RANK()	OVER ( ORDER BY n), 
		CUME_DIST()	 	OVER ( ORDER BY n) 

from ( values (1), (1), (2), (3), (3), (4) )v(n);



select  inventory_id, film_id,
		ROW_NUMBER()
		over ( partition by film_id order by inventory_id )
		as row_number
from inventory
;



select ...
from   ...
  my_agregate_function()

OVER( PARTITION BY ... ORDER BY ...)
OVER( PARTITION BY ... )
OVER(                  ORDER BY ...)
OVER( )

*/