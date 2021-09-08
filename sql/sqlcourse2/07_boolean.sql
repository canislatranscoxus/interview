/*****************************************************************************
http://www.sqlcourse2.com/boolean.html
http://www.sqlcourse2.com/items_ordered.html
http://www.sqlcourse2.com/customers.html
*****************************************************************************/


/* 1.   Select the customerid, order_date, and item from the items_ordered table 
        for all items unless they are 'Snow Shoes' or if they are 'Ear Muffs'. 
        Display the rows as long as they are not either of these two items. */
SELECT customerid, order_date, item
FROM   items_ordered
WHERE  item NOT IN ('Snow Shoes', 'Ear Muffs') ;

SELECT customerid, order_date, item
FROM items_ordered
WHERE (item <> 'Snow shoes') AND (item <> 'Ear muffs');



/* 2.   Select the item and price of all items that start with 
        the letters 'S', 'P', or 'F'. */
SELECT item, price
FROM   items_ordered
WHERE  item like 'S%' OR 
       item like 'P%' OR
       item like 'F%' 
;





