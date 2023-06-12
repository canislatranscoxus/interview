select conference,

SUM( players ) as players,
SUM( CASE WHEN year_grade = 'FR' THEN players ELSE null END ) as FR,
SUM( CASE WHEN year_grade = 'SO' THEN players ELSE null END ) as SO,
SUM( CASE WHEN year_grade = 'JR' THEN players ELSE null END ) as JR,
SUM( CASE WHEN year_grade = 'SR' THEN players ELSE null END ) as SR

FROM
	(select conference, year_grade, players
	from college_football
	) sub

group by 1
order by 1
;