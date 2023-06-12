/*
 Window Function ALIAS

https://mode.com/sql-tutorial/sql-window-functions/
*/

/*----------------------------------------------------------------------------
-- Original Query

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
WHERE 
	start_station_name in ( '4th & C St SW', '4th & M St SW', '10th & G St NW' )
	and started_at between '2020-04-01 00:00:00' and '2020-04-2 00:00:00'
;
---------------------------------------------------------------------------- */

-- Using ALIAS after WHERE clause


SELECT ride_id, start_station_name, started_at, duration_seconds,

	NTILE(  4) OVER ntile_window AS quartile,
	NTILE(  5) OVER ntile_window AS quintile,
	NTILE(100) OVER ntile_window AS percentile

FROM v_capital_bike_share
WHERE 
	start_station_name in ( '4th & C St SW', '4th & M St SW', '10th & G St NW' )
	and started_at between '2020-04-01 00:00:00' and '2020-04-2 00:00:00'
	
WINDOW ntile_window	AS
	(PARTITION BY start_station_name ORDER BY duration_seconds) 
;