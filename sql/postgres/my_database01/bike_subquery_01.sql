
select b.count_total, s.count_total
FROM

(select count(*) as bike_count_total
from capital_bike_share
) b,

(select count(*) as bike_small_count_total
from capital_bike_share_small
) s
 ;