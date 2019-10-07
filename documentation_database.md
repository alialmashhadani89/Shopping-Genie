Last Updated: 10/07/19

Current Concept
===============

Query table
* query_id int auto_increment not null (Primary Key)
* searched_phrase blob/varchar[??]

Results table
* query_id int not null (Foreign Key) from Query
* seller_id int not null (Foreign Key) from Sellers
* price double not null
* url text/varchar[??]

Sellers table
* seller_id int auto_increment not null (Primary Key)
* seller_name text/varchar[??] not null


