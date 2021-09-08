/*  Here is the problem: find the largest order amount for each salesperson 
    and the associated order number, along with the customer to whom that order belongs to. */

use sales;
select o.salesperson_id, s.name, o.cust_id, c.name, o.number, o.amount 
from Orders o, Salesperson s, Customer c
where o.salesperson_id = s.ID 
	and o.cust_id = c.ID
	and o.amount >= ALL 
    (
		select max( amount )
		from Orders t
		where   o.salesperson_id = t.salesperson_id
	)
order by o.salesperson_id, s.name, o.cust_id, c.name
;



/* this query bring max amount but no Order Number */

use sales;
select o.salesperson_id, s.name, o.cust_id, c.name, max( o.amount )
		#,o.salesperson_id ID,s.name , count(s.name) nun_orders
from Orders o, Salesperson s, Customer c
where o.salesperson_id = s.ID and o.cust_id = c.ID

group by o.salesperson_id, s.name, o.cust_id, c.name
order by o.salesperson_id, s.name, o.cust_id, c.name
;


/* answer from the article */
select salesperson_id, Number as OrderNum, Amount from Orders 
JOIN (  -- this is our subquery from above:
		SELECT salesperson_id, MAX(Amount) AS MaxOrder
		FROM Orders
		GROUP BY salesperson_id
	 ) as TopOrderAmountsPerSalesperson
USING (salesperson_id)
 where Amount = MaxOrder



