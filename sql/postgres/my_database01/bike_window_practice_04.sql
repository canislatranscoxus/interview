/*
 Write a query that shows a running total of the duration of bike rides 
 (similar to the last example), but grouped by end_terminal, 
 and with ride duration sorted in descending order. 
 
https://mode.com/sql-tutorial/sql-window-functions/
*/

select ride_id, end_station_name,
start_station_name, 
duration_seconds,

SUM(  duration_seconds) OVER ( PARTITION BY end_station_name ORDER BY duration_seconds DESC) 
AS running_total

from v_capital_bike_share;

--select * from v_capital_bike_share;