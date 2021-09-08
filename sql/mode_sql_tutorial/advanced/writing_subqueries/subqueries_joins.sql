/*---------------------------------------------------------------------------*/

SELECT COUNT(*) AS total_rows
  FROM (
        SELECT *
          FROM tutorial.crunchbase_investments_part1

         UNION ALL

        SELECT *
          FROM tutorial.crunchbase_investments_part2
       ) sub


/*---------------------------------------------------------------------------*/
/* ranks investors from the combined dataset above 
by the total number of investments they have made.  */

SELECT investor_permalink, COUNT(*) AS total_rows
FROM (
      SELECT  investor_permalink
      FROM tutorial.crunchbase_investments_part1

         UNION ALL

      SELECT  investor_permalink
      FROM tutorial.crunchbase_investments_part2
       ) sub
group by 1
order by 2
-- results: 741


SELECT investor_permalink, sum( investments ) AS num_investments
FROM (
      SELECT  investor_permalink, count(*) investments
      FROM tutorial.crunchbase_investments_part1
      group by 1

      UNION ALL

      SELECT  investor_permalink, count(*) investments
      FROM tutorial.crunchbase_investments_part2
      group by 1
      ) sub
group by 1
order by 2
-- results: 821 ms

/*---------------------------------------------------------------------------*/
/* Write a query that does the same thing as in the previous problem, 
except only for companies that are still operating. 
Hint: operating status is in tutorial.crunchbase_companies.  */


/* answer */
SELECT investments.investor_name,
       COUNT(investments.*) AS investments
  FROM tutorial.crunchbase_companies companies
  JOIN (
        SELECT *
          FROM tutorial.crunchbase_investments_part1
         
         UNION ALL
        
         SELECT *
           FROM tutorial.crunchbase_investments_part2
       ) investments
    ON investments.company_permalink = companies.permalink
 WHERE companies.status = 'operating'
 GROUP BY 1
 ORDER BY 2 DESC

/* my sol */
select i.investor_name, count(*)
from
      tutorial.crunchbase_companies c
join
    (SELECT i.investor_name, i.company_permalink
    FROM tutorial.crunchbase_investments_part1 i
    
    union all
    
    SELECT i.investor_name, i.company_permalink
    FROM tutorial.crunchbase_investments_part2 i
    ) i
on c.permalink = i.company_permalink

where c.status = 'operating'

group by 1
order by 2 desc


/*---------------------------------------------------------------------------*/
