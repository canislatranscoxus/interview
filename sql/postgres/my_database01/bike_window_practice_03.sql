/*
Write a query 
that shows the duration of each ride as 
a percentage of the total time accrued by riders from each start_station_name 

https://mode.com/sql-tutorial/sql-window-functions/
*/

select ride_id, start_station_name, duration_seconds,

SUM(  duration_seconds) OVER ( PARTITION BY start_station_name ORDER BY started_at ) 
AS running_total,

COUNT(duration_seconds) OVER ( PARTITION BY start_station_name ORDER BY started_at ) 
AS running_count,

AVG(  duration_seconds) OVER ( PARTITION BY start_station_name ORDER BY started_at ) 
AS running_avg

from v_capital_bike_share;

--select * from v_capital_bike_share;