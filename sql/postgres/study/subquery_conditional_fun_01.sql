--- select 	count( * ) from customers c;



select 	c.customer_id, c.contact_name
from customers c
where exists 
	(
		select o.customer_id 
		from orders o 
		where c.customer_id = o.customer_id 
	)
;


/*
select 	c.customer_id, c.contact_name,
 		o.order_id, o.customer_id, o.ship_city
from customers c
where 
	c.customer_id IN (select o.customer_id orders o )
;


select 	c.customer_id, c.contact_name,
 		o.order_id, o.customer_id, o.ship_city
from customers c
left join orders o 
on c.customer_id = o.customer_id
where o.customer_id is null
;


select 	c.customer_id, c.contact_name,
 		o.order_id, o.customer_id, o.ship_city
from customers c
inner join orders o 
on c.customer_id = o.customer_id;



select c.customer_id, c.contact_name
from customers c;

select o.order_id, o.customer_id, o.ship_city
from orders o;
*/