
/*
how long have been use the bikes?
We nee to take the duration time per each ride, 
then sum all the duration time of all rides.

The below query means: 
"take the sum of duration_seconds over the entire result set, in order by start_time."

*/

SELECT duration_seconds,
       SUM(duration_seconds) OVER (ORDER BY start_time) AS running_total
FROM tutorial.dc_bikeshare_q1_2012



/* To narrow the window from the entire dataset to individual groups, we use
    PARTTITION BY  */

SELECT start_terminal,
       duration_seconds,
       SUM(duration_seconds) OVER
         (PARTITION BY start_terminal ORDER BY start_time)
         AS running_total
FROM tutorial.dc_bikeshare_q1_2012
WHERE start_time < '2012-01-08'

/* ---------------------------------------------------------------------------- */



/* Write a query modification of the above example query that shows 
the duration of each ride as a percentage of the total time accrued 
by riders from each start_terminal  */

SELECT  start_terminal
        ,duration_seconds
        ,SUM(duration_seconds) OVER
          (PARTITION BY start_terminal )
        AS start_terminal_sum
        
        ,duration_seconds *100
          / SUM(duration_seconds) OVER (PARTITION BY start_terminal )
        as percent
         
FROM tutorial.dc_bikeshare_q1_2012
WHERE start_time < '2012-01-08'
order by 1, 4

/* ---------------------------------------------------------------------------- */
/* Sum, count, avg
*/
SELECT start_terminal,
       duration_seconds,
       SUM(duration_seconds) OVER
         (PARTITION BY start_terminal) AS running_total,
       COUNT(duration_seconds) OVER
         (PARTITION BY start_terminal) AS running_count,
       AVG(duration_seconds) OVER
         (PARTITION BY start_terminal) AS running_avg
  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'

/* now using order by */
SELECT start_terminal,
       duration_seconds,
       SUM(duration_seconds) OVER
         (PARTITION BY start_terminal ORDER BY start_time)
         AS running_total,
       COUNT(duration_seconds) OVER
         (PARTITION BY start_terminal ORDER BY start_time)
         AS running_count,
       AVG(duration_seconds) OVER
         (PARTITION BY start_terminal ORDER BY start_time)
         AS running_avg
  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'
/* ---------------------------------------------------------------------------- */
/* Write a query that shows a running total of the duration of bike rides 
(similar to the last example), but grouped by end_terminal, 
and with ride duration sorted in descending order.  */

SELECT  end_terminal
        ,duration_seconds
        ,SUM(duration_seconds) OVER (PARTITION BY end_terminal ORDER BY duration_seconds DESC)
          AS running_total

 FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'

/* ---------------------------------------------------------------------------- */
/* row_number() */

SELECT start_terminal,
       start_time,
       duration_seconds,
       ROW_NUMBER() OVER (ORDER BY start_time)
                    AS row_number
  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'

/* using partition by */
SELECT start_terminal,
       start_time,
       duration_seconds,
       ROW_NUMBER() OVER (PARTITION BY start_terminal
                          ORDER BY start_time)
                    AS row_number
  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'

/* ---------------------------------------------------------------------------- */
/* rank()  and dense rank() */

SELECT start_terminal,
       duration_seconds,
       start_time,
       RANK() OVER (PARTITION BY start_terminal
                    ORDER BY start_time)
              AS rank
  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'


/*
shows the 5 longest rides from each starting terminal, ordered by terminal, 
and longest to shortest rides within each terminal. 
Limit to rides that occurred before Jan. 8, 2012. 
*/

select *
from
  (SELECT start_terminal
          ,duration_seconds
          ,start_time
          ,RANK() OVER (PARTITION BY start_terminal
                        ORDER BY duration_seconds desc)
            AS rank
    FROM tutorial.dc_bikeshare_q1_2012
   WHERE start_time < '2012-01-08' ) as r

where rank <= 5

/* ---------------------------------------------------------------------------- */
/* n tiles */

/* example */
SELECT start_terminal,
       duration_seconds,
       NTILE(4) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds)
          AS quartile,
       NTILE(5) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds)
         AS quintile,
       NTILE(100) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds)
         AS percentile

FROM tutorial.dc_bikeshare_q1_2012
WHERE start_time < '2012-01-08'
ORDER BY start_terminal, duration_seconds

/* 
Write a query that shows only the duration of the trip and the percentile into which 
that duration falls (across the entire dataset—not partitioned by terminal). 
*/

SELECT  duration_seconds,
        NTILE(100) OVER ( ORDER BY duration_seconds)
        AS percentile

FROM tutorial.dc_bikeshare_q1_2012
WHERE start_time < '2012-01-08'
ORDER BY 1 desc

/* ---------------------------------------------------------------------------- */
/* Lag and Lead */

SELECT start_terminal,
       duration_seconds,
       
       LAG(duration_seconds, 1) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds) AS lag,

       LEAD(duration_seconds, 1) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds) AS lead

  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'
 ORDER BY start_terminal, duration_seconds

/* example of difference with previous row */

SELECT start_terminal,
       duration_seconds,
       duration_seconds -LAG(duration_seconds, 1) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds)
         AS difference
  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'
 ORDER BY start_terminal, duration_seconds


/* Clean Stragegy 1. remove rows with null difference */
SELECT *
  FROM (
    SELECT start_terminal,
           duration_seconds,
           duration_seconds -LAG(duration_seconds, 1) OVER
             (PARTITION BY start_terminal ORDER BY duration_seconds)
             AS difference
      FROM tutorial.dc_bikeshare_q1_2012
     WHERE start_time < '2012-01-08'
     ORDER BY start_terminal, duration_seconds
       ) sub
 WHERE sub.difference IS NOT NULL

/* Clean Stragegy 2. display Cero when difference column is null */
SELECT  start_terminal,
        duration_seconds,
        COALESCE( difference, 0 ) as difference
FROM 
        (SELECT start_terminal,
                duration_seconds,
                duration_seconds -LAG(duration_seconds, 1) OVER
                    (PARTITION BY start_terminal ORDER BY duration_seconds)
                    AS difference
        FROM tutorial.dc_bikeshare_q1_2012
        WHERE start_time < '2012-01-08'
        ORDER BY start_terminal, duration_seconds
       ) sub
 


/* ---------------------------------------------------------------------------- */
/* Window Alias 

    If we want to use multiple window functions on the same window,
    we can define a window below the WHERE clause.
    Let's see an example.
*/

/* reusing the ntile example */
SELECT start_terminal,
       duration_seconds,
       NTILE(4) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds)
         AS quartile,
       NTILE(5) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds)
         AS quintile,
       NTILE(100) OVER
         (PARTITION BY start_terminal ORDER BY duration_seconds)
         AS percentile
  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'
 ORDER BY start_terminal, duration_seconds

 /* now using a window */
SELECT start_terminal,
       duration_seconds,
       NTILE(4) OVER my_window
         AS quartile,
       NTILE(5) OVER my_window
         AS quintile,
       NTILE(100) OVER my_window
         AS percentile
  FROM tutorial.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'
 WINDOW my_window as ( partition by start_terminal order by duration_seconds )
 ORDER BY start_terminal, duration_seconds

/* ---------------------------------------------------------------------------- */

/* ---------------------------------------------------------------------------- */

