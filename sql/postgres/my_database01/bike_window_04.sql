/*
SUM duration time from the first row to the current row.

https://mode.com/sql-tutorial/sql-window-functions/
*/

select start_station_name, duration_seconds,

SUM( duration_seconds ) 
OVER (PARTITION BY start_station_name  
	  order by started_at 
	 ) 
as running_total

from v_capital_bike_share;