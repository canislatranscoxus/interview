/*
factors that influence performance:

    💀 table size
    💀 joins
    💀 aggregations

    💀 other users running queries
    💀 database performance and optimization

*/


/******************************************************************************/
/* Table size. Reduce the number of rows filtering using WHERE */

SELECT *
  FROM benn.sample_event_table
 WHERE event_date >= '2014-03-01'
   AND event_date <  '2014-04-01'


/* Limit clause is used after calculations, so it does not help just like that.
    To take advantage of LIMIT clause usea subquery.  */

SELECT COUNT(*)
FROM benn.sample_event_table
LIMIT 100
/* execution time: 424 ms  */

SELECT COUNT(*)
FROM    
    (
        SELECT *
        FROM benn.sample_event_table
        LIMIT 100
    ) sub
/* execution time: 418 ms  */

/******************************************************************************/
/* Making Joins simpler */

SELECT teams.conference AS conference,
       players.school_name,
       COUNT(1) AS players
  FROM benn.college_football_players players
  JOIN benn.college_football_teams teams
    ON teams.school_name = players.school_name
 GROUP BY 1,2
 /* execution time: 361 ms */

SELECT teams.conference,
       sub.*
  FROM (
        SELECT players.school_name,
               COUNT(*) AS players
          FROM benn.college_football_players players
         GROUP BY 1
       ) sub
  JOIN benn.college_football_teams teams
  ON teams.school_name = sub.school_name


/******************************************************************************/
/* Use EXPLAIN to identify expensive or slow steps in your query */

EXPLAIN
SELECT *
  FROM benn.sample_event_table
 WHERE event_date >= '2014-03-01'
   AND event_date < '2014-04-01'
 LIMIT 100

/******************************************************************************/
