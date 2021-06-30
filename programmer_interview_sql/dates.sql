/*
how to get current date time now

now()

current_time
current_time()

current_date
current_date()

*/

SELECT CURRENT_DATE AS date,
       CURRENT_TIME AS time,
       CURRENT_TIMESTAMP AS timestamp,
       LOCALTIME AS localtime,
       LOCALTIMESTAMP AS localtimestamp,
       NOW() AS now



/*
date1 - date2 = an_interval
*/



/*
https://www.w3schools.com/mysql/func_mysql_date_add.asp

substract an interval of time to a date

date_add( my_date, interval 7 day   ) as 7_days_later

date_add( my_date, interval 3 month ) as 3_months_later

date_add( my_date, interval 1 year  ) as 1_year_later
*/

/*
my_time_stamp   + interval '5 seconds' 
my_date         + interval '1 week'
my_date         + interval '7 days'
my_date         + interval '3 months'
my_date         + interval '1 year'


*/


/*
substract an interval of time to a date

date_sub( my_date, interval 7 day   ) as 7_days_ago

date_sub( my_date, interval 3 month ) as 3_months_ago

date_sub( my_date, interval 1 year  ) as 1_year_ago


*/

/*
get years from interval
*/

/*
get months from interval
*/

/*
get days from interval
*/



