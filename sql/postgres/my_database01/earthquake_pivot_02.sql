/*
Pivoting columns to rows
https://mode.com/sql-tutorial/sql-pivot-table/
*/

select y.year, e.magnitude,

	case y.year
	  when 2000 then year_2000
	  when 2001 then year_2001
	  when 2002 then year_2002
	  when 2003 then year_2003
	  when 2004 then year_2004
	  when 2005 then year_2005
	  when 2006 then year_2006
	  when 2007 then year_2007
	  when 2008 then year_2008
	  when 2009 then year_2009
	  when 2010 then year_2010
	  when 2011 then year_2011
	  when 2012 then year_2012
	  else null 
	end
	as num_earthquakes

from earthquake e
cross join

	(SELECT year
	FROM 
		(VALUES (2000),(2001),(2002),(2003),(2004),(2005),(2006),
				   (2007),(2008),(2009),(2010),(2011),(2012)
		) v(year)
	) y			   
;			   