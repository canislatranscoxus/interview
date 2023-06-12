
DROP VIEW IF EXISTS v_capital_bike_share;

CREATE OR REPLACE VIEW v_capital_bike_share AS

SELECT ride_id, 
  (ended_at - started_at ) as "duration_ts",
  EXTRACT( EPOCH FROM ( ended_at - started_at )) as "duration_seconds",
  
  started_at, 
  ended_at, 
  start_station_name, end_station_name

FROM capital_bike_share
;
