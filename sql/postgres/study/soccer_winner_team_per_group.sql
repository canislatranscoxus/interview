/*
Football Soccer World Cup in 2014.

Given 
database: my_database01
schema  :soccer
tables  :
	* team and 
	* match

write  a SQL query that return The team that scored more goals
per Group in the worldcup.

Explanation: in the winners view we use RANK() function, 
             because we consider draws scenarios,
             such as Group D, Costa Rica and Uruguay have 4 goals,
             so both are in first place of group D, 
             both teams are winners.
 

*/

set search_path to soccer;

--select * from match;
--select * from team;

with team_goals as
(
  select home_team_goals as goals, home_team_id as team_id
  from match
  UNION ALL
  select away_team_goals as goals, away_team_id as team_id
  from match
),

goals as
(
  select team_id, sum( goals ) as goals
	from team_goals
	group by 1
),

group_team_goals as
(
  select t.group, t.id, t.name, g.goals
	from team  as t
	join goals as g on t.id = g.team_id
),

winners as 
(
  select t.group, t.id, t.name, t.goals,
	     rank() over ( partition by t.group order by t.goals desc ) as goal_rank
  from group_team_goals as t
)
select *
from winners
where goal_rank = 1
;
