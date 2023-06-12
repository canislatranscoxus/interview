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

-- Solution 2

select 	c.id, c.name, 'California' as "university"
FROM		groups_california c
WHERE 	c.id not in 
	(select c.id
	FROM		groups_california c
	JOIN 		groups_newyork    n	ON c.id = n.id )

UNION

select 	n.id, n.name, 'New York' as "university"
FROM		groups_newyork n
WHERE 	n.id not in 
	(select c.id
	FROM		groups_california c
	JOIN 		groups_newyork    n	ON c.id = n.id )


;	

