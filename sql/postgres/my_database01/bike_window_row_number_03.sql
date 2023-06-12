/*
 SELECT hte top 5 (first 5) of each start_stattion_name
 
https://mode.com/sql-tutorial/sql-window-functions/
*/

SELECT ride_id, start_station_name, duration_seconds, row_num

FROM 

(SELECT ride_id, start_station_name, duration_seconds,

 ROW_NUMBER() OVER ( PARTITION BY start_station_name ORDER BY started_at ) 
 AS row_num

 FROM v_capital_bike_share
) t

WHERE row_num <= 3
;

--select * from v_capital_bike_share;