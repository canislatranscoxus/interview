/*
get latitude and longitude from location

sample location:
    (37.709725805163, -122.413623946206)


*/

SELECT location
       ,lat
       ,substring( location, 2, strpos( location, ','  ) -2 ) lat_clean  
       ,strpos( location, ','  ) pos_comma

       ,lon
       ,trim(
          substring( location, strpos( location, ','  ) +1, 
                     length(location) - strpos( location, ','  ) -1 ) 
        )lon_clean  
       
  FROM tutorial.sf_crime_incidents_2014_01

limit 10

/* concat */
SELECT incidnt_num,
       day_of_week,
       LEFT(date, 10) AS cleaned_date,
       CONCAT(day_of_week, ', ', LEFT(date, 10)) AS day_and_date
  FROM tutorial.sf_crime_incidents_2014_01


select date
,substr( date, 7, 4 ) || '-' ||
 substr( date, 1, 2 ) || '-' ||
 substr( date, 4, 2 ) "YYYY_MM_DD"
FROM tutorial.sf_crime_incidents_2014_01
limit 10

/* upper lower case */
select     upper( left( category, 1  )  )
        || lower( RIGHT( category, length( category ) -1 )  )  "Category"

FROM tutorial.sf_crime_incidents_2014_01
limit 10


/* adding date + time, and one week later column */
select  date, time   

,(SUBSTR(date, 7, 4) || '-' || LEFT(date, 2) || '-' || SUBSTR(date, 4, 2))::date
  + ( time )::time accurate_ts

,(SUBSTR(date, 7, 4) || '-' || LEFT(date, 2) || '-' || SUBSTR(date, 4, 2))::date
  + ( time )::time
  + interval '1 week'  as "1 week later"

FROM tutorial.sf_crime_incidents_2014_01
limit 10

SELECT incidnt_num,
       (SUBSTR(date, 7, 4) || '-' || LEFT(date, 2) || '-' || SUBSTR(date, 4, 2) 
            || ' ' || time || ':00')::timestamp AS timestamp,
       (SUBSTR(date, 7, 4) || '-' || LEFT(date, 2) || '-' || SUBSTR(date, 4, 2) 
            || ' ' || time || ':00')::timestamp

        + INTERVAL '1 week' AS timestamp_plus_interval
  FROM tutorial.sf_crime_incidents_2014_01


/* extract parts of a date */
SELECT cleaned_date,
       EXTRACT('year'   FROM cleaned_date) AS year,
       EXTRACT('month'  FROM cleaned_date) AS month,
       EXTRACT('day'    FROM cleaned_date) AS day,
       EXTRACT('hour'   FROM cleaned_date) AS hour,
       EXTRACT('minute' FROM cleaned_date) AS minute,
       EXTRACT('second' FROM cleaned_date) AS second,
       EXTRACT('decade' FROM cleaned_date) AS decade,
       EXTRACT('dow'    FROM cleaned_date) AS day_of_week
  FROM tutorial.sf_crime_incidents_cleandate

/* count number of accidents per week */
select   date_trunc( 'week', cleaned_date  )::date as week
        ,count( incidnt_num )
FROM tutorial.sf_crime_incidents_cleandate
group by 1
order by 1
limit 10


/* elapsed time using pacific standard time zone */
SELECT  incidnt_num
        ,cleaned_date
        ,now() at time zone 'PST' as "now"
        ,now() at time zone 'PST' - cleaned_date::timestamp as elapsed_time

FROM tutorial.sf_crime_incidents_cleandate
limit 10


