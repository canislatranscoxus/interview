/*
ROW_NUMBER
https://mode.com/sql-tutorial/sql-window-functions/
*/

SELECT start_station_name, duration_seconds,

ROW_NUMBER()
OVER (PARTITION BY start_station_name ORDER BY started_at ) 
as row_num

FROM v_capital_bike_share;