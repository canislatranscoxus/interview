/*
 Window Function NTILE

Write a query that shows only the duration of the trip and the percentile 
into which that duration falls (across the entire dataset—not partitioned by terminal). 

https://mode.com/sql-tutorial/sql-window-functions/
*/

select duration_seconds,

NTILE(100) 
OVER (ORDER BY duration_seconds ) 
AS percentile

from v_capital_bike_share
where 
--start_station_name in ( '4th & C St SW', '4th & M St SW', '10th & G St NW' ) and 
started_at between '2020-04-01 00:00:00' and '2020-04-01 09:00:00'
;

--select * from v_capital_bike_share;