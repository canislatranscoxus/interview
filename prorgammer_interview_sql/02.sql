/* Practice SQL Interview Question #2
 

This question was asked in a Google interview: Given the 2 tables below, User and UserHistory:

User
----------
user_id
name
phone_num


UserHistory
------------
user_id
date
action
*/

/* 1.   Write a SQL query that returns the name, phone number and most recent date for 
        any user that has logged in over the last 30 days (you can tell a user has logged in 
        if the action field in UserHistory is set to "logged_on").
        Every time a user logs in a new row is inserted into the UserHistory table with user_id,
        current date and action (where action = "logged_on"). */
select name, phone_num
from   user_history h join user u on h.user_id = u.user_id 
where  h.action = 'logged_on'
  and  datediff(day, date(), date  ) <= 30;

/* 2.   Write a SQL query to determine which user_ids in the User table are not contained in 
        the UserHistory table (assume the UserHistory table has a subset of the user_ids in 
        User table). Do not use the SQL MINUS statement. 
        Note: the UserHistory table can have multiple entries for each user_id. */
select name
from user u left join user_history h on u.user_id  = h.user_id
where h.user_id IS NULL
;  

select name
from user u 
where u.user_id not in 
( select disctinc name 
  from user_history )
;  

select name
from user u 
where u.user_id not in 
( select user_id
  from user_history
  group by user_id )
;  



/* Note that your SQL should be compatible with MySQL 5.0, and avoid using subqueries. */