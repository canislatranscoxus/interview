/*
 Window Function LAG LEAD

We wrap the query and remove rows where the difference in null.
Just to make it cleaner.

https://mode.com/sql-tutorial/sql-window-functions/
*/

SELECT * 
FROM
	(select start_station_name, duration_seconds,

	duration_seconds -
	LAG( duration_seconds, 1 ) 
	OVER ( PARTITION BY start_station_name ORDER BY duration_seconds ) 
	AS lag_diff

	from v_capital_bike_share
	where 
	--start_station_name in ( '4th & C St SW', '4th & M St SW', '10th & G St NW' ) and 
	started_at between '2020-04-01 00:00:00' and '2020-04-01 09:00:00'
	) t

where t.lag_diff is not null
;

--select * from v_capital_bike_share;