/*
Write a query that shows the 5 longest rides from each starting terminal, 
ordered by terminal, and longest to shortest rides within each terminal. 
Limit to rides that occurred before Jan. 8, 2012. 
 
https://mode.com/sql-tutorial/sql-window-functions/
*/

SELECT ride_id, start_station_name, duration_seconds, started_at, rank
FROM
	(SELECT ride_id, start_station_name, duration_seconds, started_at,
	 RANK() OVER ( PARTITION BY start_station_name ORDER BY duration_seconds DESC) 
	 AS rank
	 FROM v_capital_bike_share
	) t 

WHERE t.rank <= 5
;

--select * from v_capital_bike_share;