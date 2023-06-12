
DROP TABLE IF EXISTS groups_california;
CREATE TABLE groups_california (
id int,
name varchar(50)
);

DROP TABLE IF EXISTS groups_newyork;
CREATE TABLE groups_newyork (
id int,
name varchar(50)
);

INSERT INTO groups_california(id, name ) values
(10, 'chess'	),
(20, 'wrestling'),
(30, 'box'		)
;

INSERT INTO groups_newyork(id, name ) values
(20, 'wrestling'),
(30, 'box'		),
(40, 'fencing'	)
;