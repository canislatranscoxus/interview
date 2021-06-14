/*********************************************************************************
we can use subqueries in

         SELECT
         FROM
         WHERE



*********************************************************************************/

/* small example */

select sub.*
FROM 
(select id, incidnt_num, category, descript, resolution
 from tutorial.sf_crime_incidents_2014_01
 where lower( descript ) like 'warrant arrest%'
 ) sub

where sub.resolution = 'NONE'
limit 10


/*
What if you wanted to figure out how many incidents get reported on each day of the week? 
Better yet, what if you wanted to know how many incidents happen, on average, 
on a Friday in December? In January? There are two steps to this process: 
counting the number of incidents each day (inner query), 
then determining the monthly average (outer query):
*/

select left( date, 2  ) as month
        ,day_of_week
        ,avg( incidents ) avg_incidents
FROM
  (SELECT  date
          ,day_of_week
          ,count( incidnt_num ) AS incidents 
   FROM tutorial.sf_crime_incidents_2014_01
   GROUP BY 1,2
   ) s

group by 1,2 
order by 1,2

/*
Write a query that displays the average number of monthly incidents for each category. 
Hint: use tutorial.sf_crime_incidents_cleandate to make your life a little easier. 
*/

select category
        ,avg( incidents )
FROM
    (select category
           ,extract( 'month' from cleaned_date ) as "month"
           ,count(incidnt_num) as incidents
    from tutorial.sf_crime_incidents_cleandate
    group by 1, 2 ) s
group by 1
order by 1


/* Subqueries in conditional logic */

SELECT *
  FROM tutorial.sf_crime_incidents_2014_01
 WHERE Date = (SELECT MIN(date)
                 FROM tutorial.sf_crime_incidents_2014_01
              )

SELECT *
  FROM tutorial.sf_crime_incidents_2014_01
 WHERE Date IN (SELECT date
                 FROM tutorial.sf_crime_incidents_2014_01
                ORDER BY date
                LIMIT 5
              )


/* Joining subqueries */

SELECT *
  FROM tutorial.sf_crime_incidents_2014_01 incidents
  JOIN ( SELECT date
           FROM tutorial.sf_crime_incidents_2014_01
          ORDER BY date
          LIMIT 5
       ) sub
    ON incidents.date = sub.date


/* join subquery */

SELECT incidents.*,
       sub.incidents AS incidents_that_day
  FROM tutorial.sf_crime_incidents_2014_01 incidents
  JOIN ( SELECT date,
          COUNT(incidnt_num) AS incidents
           FROM tutorial.sf_crime_incidents_2014_01
          GROUP BY 1
       ) sub
    ON incidents.date = sub.date
 ORDER BY sub.incidents DESC, time

/*
Write a query that displays all rows from the three categories with the fewest incidents reported. 
*/

SELECT  i.category, i.incidnt_num, i.descript, i.date
from    tutorial.sf_crime_incidents_2014_01 i
join 
  (SELECT   category, count( incidnt_num ) count_incidents
  FROM      tutorial.sf_crime_incidents_2014_01
  group by 1
  order by 2
  limit 3) c

on i.category = c.category
order by c.category, i.date, i.incidnt_num 



/* ---------------------------------------------------------------------------
Imagine you'd like to aggregate all of the companies receiving investment and 
companies acquired each month  */

/*count all rows, but may be we count duplicated rows....*/
SELECT  COUNT(*) acquisitions
        , (SELECT COUNT( distinct company_permalink ) investments FROM tutorial.crunchbase_investments) 
FROM tutorial.crunchbase_acquisitions

/* results: 899 ms
acquisitions	investments
7314	           22421

*/


SELECT  ( select COUNT( distinct company_permalink ) FROM tutorial.crunchbase_acquisitions ) acquisitions
        ,(SELECT COUNT( distinct company_permalink ) FROM tutorial.crunchbase_investments  ) investments
/* results: 935 ms */


/* count specifying DISTINCT */

SELECT  coalesce( a.acquired_month, i.funded_month ) as month
        ,a.acquisitions
        ,i.investments
from
      ( select  acquired_month 
                ,COUNT( DISTINCT company_permalink ) acquisitions
        FROM tutorial.crunchbase_acquisitions 
        group by 1) a
full join              
      ( SELECT  funded_month
                ,COUNT( DISTINCT company_permalink ) investments
        FROM tutorial.crunchbase_investments  
        group by 1) i

on a.acquired_month = i.funded_month        
order by 1 desc        
/* results: 874 ms */

/*---------------------------------------------------------------------------*/

/* count number of different months */

select count(*)
from
(select funded_month
 FROM tutorial.crunchbase_investments
 group by 1) i



/* ranks all of the results according to how many incidents were reported in a given day. 
It does this by aggregating the total number of incidents each day in the inner query, 
then using those values to sort the outer query: */

SELECT incidents.*,
       sub.incidents AS incidents_that_day
  FROM tutorial.sf_crime_incidents_2014_01 incidents
  JOIN ( SELECT date,
          COUNT(incidnt_num) AS incidents
           FROM tutorial.sf_crime_incidents_2014_01
          GROUP BY 1
       ) sub
    ON incidents.date = sub.date
 ORDER BY sub.incidents DESC, time


/* Write a query that displays all rows from the three categories with the fewest incidents reported. */

-- 443 ms
select * 
from tutorial.sf_crime_incidents_2014_01 i
where category in
  (select category
  FROM tutorial.sf_crime_incidents_2014_01
  group by category
  order by count(distinct incidnt_num )
  limit 3) 
  order by i.category, i.date
  

-- 489 ms
  SELECT incidents.*,
       sub.count AS total_incidents_in_category
  FROM tutorial.sf_crime_incidents_2014_01 incidents
  JOIN (
        SELECT category,
               COUNT(*) AS count
          FROM tutorial.sf_crime_incidents_2014_01
         GROUP BY 1
         ORDER BY 2
         LIMIT 3
       ) sub
    ON sub.category = incidents.category

/*---------------------------------------------------------------------------*/
/*
Write a query that counts the number of companies founded and acquired 
by quarter starting in Q1 2012. Create the aggregations in two separate queries, 
then join them. 
*/


select  company_permalink
        ,count( distinct company_permalink )
FROM tutorial.crunchbase_acquisitions a
where a.acquired_quarter = '2012-Q1'
group by 1

/*---------------------------------------------------------------------------*/

/*
Counts the number of companies founded and acquired by quarter starting in Q1 2012. 
Create the aggregations in two separate queries, then join them. 
*/

select  coalesce( c.founded_quarter, a.acquired_quarter ) as quarter
        ,c.funded
        ,a.acquisitions
from 
    (select  c.founded_quarter
            ,count( c.permalink ) as funded
    FROM tutorial.crunchbase_companies c
    where c.founded_quarter  >= '2012-Q1'
    GROUP by 1) c

left join 

    (select a.acquired_quarter
            ,count( distinct company_permalink ) as acquisitions
    FROM tutorial.crunchbase_acquisitions a
    where a.acquired_quarter >= '2012-Q1'
    group by 1) a

on c.founded_quarter = a.acquired_quarter

order by 1

/* answer */
SELECT COALESCE(companies.quarter, acquisitions.quarter) AS quarter,
           companies.companies_founded,
           acquisitions.companies_acquired
      FROM (
            SELECT founded_quarter AS quarter,
                   COUNT(permalink) AS companies_founded
              FROM tutorial.crunchbase_companies
             WHERE founded_year >= 2012
             GROUP BY 1
           ) companies
      
      LEFT JOIN (
            SELECT acquired_quarter AS quarter,
                   COUNT(DISTINCT company_permalink) AS companies_acquired
              FROM tutorial.crunchbase_acquisitions
             WHERE acquired_year >= 2012
             GROUP BY 1
           ) acquisitions
        
        ON companies.quarter = acquisitions.quarter
     ORDER BY 1
/*---------------------------------------------------------------------------*/


