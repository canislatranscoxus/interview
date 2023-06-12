/*
 Window Function NTILE

Write a query that shows only the duration of the trip and the percentile 
into which that duration falls (across the entire dataset—not partitioned by terminal). 

https://mode.com/sql-tutorial/sql-window-functions/
*/

SELECT start_station_name, duration_seconds,

LAG( duration_seconds, 1 ) 
OVER ( PARTITION BY start_station_name ORDER BY duration_seconds ) 
AS lag,

LEAD( duration_seconds, 1 )
OVER ( PARTITION BY start_station_name ORDER BY duration_seconds )
AS lead

FROM v_capital_bike_share
WHERE started_at between '2020-04-01 00:00:00' and '2020-04-01 09:00:00'
;
