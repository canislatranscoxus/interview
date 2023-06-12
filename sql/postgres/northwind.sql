select 	o.order_id, o.ship_country, 
		c.customer_id, c.company_name, c.contact_name 

from 		orders o 
inner join 	customers c 
on o.customer_id = c.customer_id;




