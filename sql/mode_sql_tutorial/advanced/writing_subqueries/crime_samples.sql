/*
        Given a crime table, calculate the percent of crime that friday crime represent.
        Use table tutorial.sf_crime_incidents_2014_01,
        suppose field incidnt_num is unique in the table.
        We have the next data 

-- Friday count:  5,051
-- total  count: 30,400
-- percent = 100.0 * 5,051 / 30,400

links:
        https://mode.com/sql-tutorial/sql-sub-queries/
        https://app.mode.com/editor/canis/reports/b162f55d51ec/queries/9c7f8639c6a6
*/

-- we need to use 2 subqueries as tables. Next do the percent maths.

SELECT  f.friday_incidents, t.total_incidents, 
        100.00 * f.friday_incidents/ t.total_incidents as "Friday - Total Crime percent ( 0 - 100 )"
        
FROM (  Select count( incidnt_num ) as total_incidents
        from tutorial.sf_crime_incidents_2014_01 ) t,

     (  select count( incidnt_num ) as friday_incidents 
        from tutorial.sf_crime_incidents_2014_01
        WHERE day_of_week = 'Friday'
     ) f
;      
         