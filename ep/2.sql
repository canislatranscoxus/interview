select group_id, winner_id
FROM 

(
select group_id, winner_id, 

  ROW_NUMBER() OVER ( PARTITION BY group_id  ORDER BY total_score DESC, winner_id )
  as row_num

from 

(
SELECT p.group_id, p.player_id as winner_id ,
  COALESCE(  MAX( s.score ), 0 ) as total_score

FROM players p
left JOIN 
	(select player_id, sum( score ) as score
	from
	    (
	    select first_player as player_id,
		first_score  as score
	    from matches 
	    UNION
	    select second_player as player_id,
		second_score  as score
	    from matches 
	    ) as scores
	group by 1
	) as s

ON p.player_id = s.player_id



GROUP BY 1, 2
--order by MAX( s.score ) DESC
) as r

) as winners

where row_num = 1

;

