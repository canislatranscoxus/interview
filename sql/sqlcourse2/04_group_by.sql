/*
http://www.sqlcourse2.com/groupby.html

http://www.sqlcourse2.com/items_ordered.html
http://www.sqlcourse2.com/customers.html

*/

/* For example, take a look at the items_ordered table. 
        Let's say you want to group everything of quantity 1 together, 
        everything of quantity 2 together, everything of quantity 3 together, etc. 
        If you would like to determine what the largest cost item is for each 
        grouped quantity (all quantity 1's, all quantity 2's, all quantity 3's, etc.), 
        you would enter:*/

SELECT o.quantity, o.price, o.item
FROM   items_ordered o
WHERE  o.price >= ALL (
        SELECT max( t.price )
        FROM   items_ordered t
        WHERE  o.quantity = t.quantity
        GROUP BY quantity )
ORDER BY quantity;

/* 1.   How many people are in each unique state in the customers table? 
        Select the state and display the number of people in each. 
        Hint: count is used to count rows in a column, sum works on numeric data only. */
SELECT   state, count(*)
FROM     customers
GROUP BY state
ORDER BY count(*) desc, state;

/* 2.   From the items_ordered table, select the item, maximum price, 
        and minimum price for each specific item in the table. 
        Hint: The items will need to be broken up into separate groups. */
SELECT   item, min(price), max(price)
FROM     items_ordered
GROUP BY item
--ORDER BY item
;

/* 3.   How many orders did each customer make? Use the items_ordered table. 
        Select the customerid, number of orders they made, and the sum of their orders. 
        Click the Group By answers link below if you have any problems. */
SELECT   customerid, count(*), 
         sum( quantity * price )

FROM     items_ordered
GROUP BY customerid
ORDER BY customerid
;





