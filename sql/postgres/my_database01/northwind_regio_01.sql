select	r.region_id, t.territory_id,
		r.region_description,
		t.territory_description
from region 	 r 
join territories t ON r.region_id = t.region_id
order by 1, 2
;