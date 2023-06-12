/*
 Window Function NTILE
https://mode.com/sql-tutorial/sql-window-functions/
*/

select ride_id, start_station_name, started_at, duration_seconds,

NTILE(4)
OVER (PARTITION BY start_station_name ORDER BY duration_seconds)
AS quartile,

NTILE(5)
OVER (PARTITION BY start_station_name ORDER BY duration_seconds)
AS quintile,


NTILE(100) 
OVER ( PARTITION BY start_station_name ORDER BY duration_seconds ) 
AS percentile

from v_capital_bike_share
--where start_station_name in ( '4th & C St SW', '4th & M St SW', '10th & G St NW' )
--and started_at between '2020-04-01 00:00:00' and '2020-04-15 00:00:00'
;

--select * from v_capital_bike_share;