/*
get the latest ride in a start station

If you'd like to narrow the window from the entire dataset 
to individual groups within the dataset, you can use PARTITION BY to do so.

https://mode.com/sql-tutorial/sql-window-functions/
*/

-- "10th & E St NW"	"2020-04-30"	"2020-04-30 17:23:04"

select start_station_name, 
DATE(started_at) as started_date,
max( started_at )
 --started_at 


from v_capital_bike_share
--where start_station_name = '10th & E St NW'
group by 1, 2
order by 1, 2
;