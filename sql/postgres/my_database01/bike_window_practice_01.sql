/*
Write a query 
that shows the duration of each ride as 
a percentage of the total time accrued by riders from each start_station_name 

https://mode.com/sql-tutorial/sql-window-functions/
*/

select ride_id, start_station_name, duration_seconds,

SUM(duration_seconds) 
OVER ( PARTITION BY start_station_name ) 
AS running_total,

100 * duration_seconds /
(SUM(duration_seconds) OVER ( PARTITION BY start_station_name ) ) 
AS ride_percent

from v_capital_bike_share;

--select * from v_capital_bike_share;