--select * from products;
--select *  from orders;

select * 
from
	(select ship_country, employee_id, count(*) as num_ship
	from orders
	where ship_country in ( 'Denmark', 'France', 'Sweden' )
	group by 1, 2
	limit 10
	) t
order by 1
;
