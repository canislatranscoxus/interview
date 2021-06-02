/*****************************************************************************
http://www.sqlcourse2.com/joins.html
http://www.sqlcourse2.com/items_ordered.html
http://www.sqlcourse2.com/customers.html
*****************************************************************************/


/* 1.   Write a query using a join to determine which items were ordered 
        by each of the customers in the customers table. 
        Select the customerid, firstname, lastname, order_date, item, and price 
        for everything each customer purchased in the items_ordered table. */
SELECT c.customerid, c.firstname,   
       c.lastname, 
       o.order_date, o.item, o.price

FROM   items_ordered o JOIN customers c
ON o.customerid = c.customerid
ORDER BY c.customerid;


/* 2.   Repeat exercise #1, however display the results sorted by state in descending order. */
SELECT c.state, 
       c.customerid, c.firstname,   
       c.lastname, 
       o.order_date, o.item, o.price

FROM   items_ordered o JOIN customers c
ON o.customerid = c.customerid
ORDER BY state DESC;
