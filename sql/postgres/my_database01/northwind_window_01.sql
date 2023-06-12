--select	* from region;

--select count(*) from orders; -- 830

select ship_country, 

	SUM( count_ship ) OVER ( ORDER BY count_ship )
	as total_ship,
	
	count_ship,
	
	100 * count_ship
	/ 
	SUM( count_ship ) OVER ( ORDER BY count_ship )
	as percent_ship
	
FROM 

(
	select ship_country, count(*) as count_ship
	from orders
	where ship_country like 'S%'
	group by ship_country
	order by 1
) t; 
