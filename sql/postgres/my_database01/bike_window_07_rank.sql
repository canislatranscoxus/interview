/*
 Window Function RANK
https://mode.com/sql-tutorial/sql-window-functions/
*/

select ride_id, start_station_name, started_at, duration_seconds,

RANK() 
OVER ( PARTITION BY start_station_name ORDER BY started_at ) 
AS row_num

from v_capital_bike_share
where start_station_name in ( '4th & C St SW', '4th & M St SW', '10th & G St NW' )
and started_at between '2020-04-01 00:00:00' and '2020-04-03 00:00:00'
;

--select * from v_capital_bike_share;

/*select start_station_name, started_at, count(*)
from v_capital_bike_share
group by 1, 2 
having count(*) > 1
order by 2
;*/