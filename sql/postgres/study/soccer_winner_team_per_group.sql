/*
Football Soccer World Cup in 2014.

Given tables:
	* team and 
	* match

write  a SQL query that return The team that scored more goals
per Group in the worldcup.


*/

set search_path to soccer;


WITH

match_team_goals as 
(select home_team_id as id, home_team_goals as goals
from soccer.match
UNION
select away_team_id as id, away_team_goals as goals
from soccer.match
),

scores as
(
select id, sum( goals ) as goals
	from match_team_goals
group by 1	
),

team_goals as
(
select t.group, s.goals, t.id, t.name 
from team t
left join scores s on t.id = s.id
--order by 1
),

winners as
(
select g.group, g.goals, g.id, g.name, 
  ROW_NUMBER() OVER (PARTITION BY g.group  ORDER BY g.goals DESC, g.id )
  as row_number
from team_goals as g
)	

select w.group, w.name
from winners as w
where row_number = 1
	;