SELECT employee_id,

SUM( CASE WHEN ship_country = 'Denmark' THEN num_ship ELSE null END ) as Denmark,
SUM( CASE WHEN ship_country = 'France'  THEN num_ship ELSE null END ) as France,
SUM( CASE WHEN ship_country = 'Sweden'  THEN num_ship ELSE null END ) as Sweden

FROM
( select ship_country, employee_id, count(*) as num_ship
  from orders
  where ship_country in ( 'Denmark','France','Sweden' )
  group by 1, 2
  limit 10
) t

group by 1
;