/* Outer Join example

We have 2 tables for groups of extracurricular activities for universities.
We want to see which groups are unique and only can be practiced just in 
one university.

Having  
table: groups_california
+----+-----------+
| id |   name    |
|----|-----------|
| 10 | chess     |
| 20 | wrestling |
| 30 | box       |
+----+-----------+

table: groups_newyork
+----+-----------+
| id |   name    |
|----|-----------|
| 20 | wrestling |
| 30 | box       |
| 40 | fencing   |
+----+-----------+

Expected Output
+----+-----------+------------+
| id |   name    | university |
|----|-----------|------------+
| 10 | chess     | California |
| 40 | fencing   | New York   |
+----+-----------+------------+

Create a SQL query that return the expected Output.
*/

-- Solution 1

select 	case 
			when c.id is not null then c.id 
			when n.id is not null then n.id 
		end as id,
		
		case 
			when c.id is not null then c.name 
			when n.id is not null then n.name
		end as group_name,		
		
		case 
			when c.id is not null then 'California'
			when n.id is not null then 'New York'
		end as university
		

FROM		groups_california c
full OUTER JOIN 	groups_newyork n	ON c.id = n.id

where	c.id is null or n.id is null
;