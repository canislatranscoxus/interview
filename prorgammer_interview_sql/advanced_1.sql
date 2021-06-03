/*  We want to retrieve the names of all salespeople that have more than 1 order 
    from the tables above. You can assume that each salesperson only has one ID */

use sales;
select s.name
		#o.salesperson_id ,s.name , count(s.name)
from Orders o, Salesperson s
where o.salesperson_id = s.ID
group by o.salesperson_id, s.name
having count(o.salesperson_id) > 1
;




