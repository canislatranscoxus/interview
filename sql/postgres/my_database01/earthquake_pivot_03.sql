/* play with this
*/

-- create a table with 13 rows
VALUES (2000),(2001),(2002),(2003),(2004),(2005),(2006),
				   (2007),(2008),(2009),(2010),(2011),(2012)


-- subquery to create table, and rename the column
-- this subquery must be inside a bigger query or you will get an error.
(
  VALUES (2000),(2001),(2002),(2003),(2004),(2005),(2006),
         (2007),(2008),(2009),(2010),(2011),(2012)
) v(year)

-- wrap the subquery to select the table of years

SELECT year
FROM 
		(VALUES (2000),(2001),(2002),(2003),(2004),(2005),(2006),
				   (2007),(2008),(2009),(2010),(2011),(2012)
		) v(year)

