drop table if exists capital_bike_share;

create table capital_bike_share(

ride_id					varchar(20),
rideable_type			varchar(100),
started_at				timestamp,
ended_at				timestamp,
start_station_name		varchar(100),
start_station_id		int,
end_station_name		varchar(100),
end_station_id			int,
start_lat				double precision,
start_lng				double precision,
end_lat					double precision,
end_lng					double precision,
member_casual			varchar(20)
);


drop table if exists capital_bike_share_small;
CREATE TABLE capital_bike_share_small AS
  TABLE capital_bike_share;
