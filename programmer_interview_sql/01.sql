/*
http://www.programmerinterview.com/database-sql/practice-interview-question-1/

*/




/* a. The names of all salespeople that have an order with Samsonic. */
select  s.Name
# o.number, o.salesperson_id, 
from Orders o join Salesperson s ON o.salesperson_id = s.ID
			  join Customer    c ON o.cust_id        = c.ID
where c.Name = 'Samsonic'              
order by o.number;

/* b. The names of all salespeople that do not have any order with Samsonic. */
select Name
from Salesperson
where Name not in 
    (select  s.Name
    from Orders o join Salesperson s ON o.salesperson_id = s.ID
                join Customer    c ON o.cust_id        = c.ID
    where c.Name = 'Samsonic' 
    group by s.Name);


select s1.name
from Salesperson s1 left join
	(	select  distinct s.ID, s.Name
		from 	Orders o join Salesperson s ON o.salesperson_id = s.ID
					  join Customer    c ON o.cust_id        = c.ID
		where 	c.Name = 'Samsonic' 
    ) samsonic_sellers
    ON s1.ID = samsonic_sellers.ID
WHERE samsonic_sellers.ID is NULL;

/* c. The names of salespeople that have 2 or more orders. */
select  s.Name
from 	Orders o join Salesperson s ON o.salesperson_id = s.ID
group by s.Name
having count(*) >= 2;


/* d. Write a SQL statement to insert rows into a table called highAchiever(Name, Age), 
where a salesperson must have a salary of 100,000 or greater to be included in the table. */
insert into highAchiever
	select Name, Age
	from Salesperson 
	where salary >= 100000 ;
