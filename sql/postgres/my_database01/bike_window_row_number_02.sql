/*
 Write a query that shows a running total of the duration of bike rides 
 (similar to the last example), but grouped by end_terminal, 
 and with ride duration sorted in descending order. 
 
https://mode.com/sql-tutorial/sql-window-functions/
*/

select ride_id, start_station_name, 
--end_station_name,
duration_seconds,

ROW_NUMBER() OVER ( PARTITION BY start_station_name ORDER BY started_at ) 
AS row_num

from v_capital_bike_share;

--select * from v_capital_bike_share;