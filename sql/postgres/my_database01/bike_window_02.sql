/*
SUM duration time from the first row to the current row.

https://mode.com/sql-tutorial/sql-window-functions/
*/

select duration_ts,

SUM(duration_ts) OVER ( order by started_at ) as running_total

from v_capital_bike_share;