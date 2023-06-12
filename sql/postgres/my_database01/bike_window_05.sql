/*
SUM duration time from the first row to the current row.

https://mode.com/sql-tutorial/sql-window-functions/
*/

select start_station_name, duration_seconds,

SUM( duration_seconds ) 
OVER (PARTITION BY start_station_name ORDER BY started_at ) 
as running_total,

COUNT( duration_seconds ) 
OVER (PARTITION BY start_station_name ORDER BY started_at ) 
as running_count,

AVG( duration_seconds )
OVER (PARTITION BY start_station_name ORDER BY started_at )
as running_avg


from v_capital_bike_share;


--select * from  v_capital_bike_share;