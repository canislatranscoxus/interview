

/* select name and salary, and order by highest to lowest salary */
select name, salary
from   Salesperson
order by salary desc

/* select sellers with the top 3 highest salaries */
select name, salary
from   Salesperson
order by salary desc
limit 3


/* select the seller with the 3rd highest salary  */
use sales;
select name, salary 
from 
(select name, salary
from   Salesperson
order by salary desc
limit 3) t
order by salary
limit 1
;
