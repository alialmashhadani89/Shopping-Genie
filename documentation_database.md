Last Updated: 10/21/19




Current Iteration Creation Statements
======
Iteration 1

NOTE: Please name the database "shopping_genie"

CREATE TABLE queries(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
search_term VARCHAR(255));

CREATE TABLE brands(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255));

CREATE TABLE sellers(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255));

CREATE TABLE results(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
qid INT NOT NULL,
sid INT NOT NULL,
bid INT NOT NULL,
price DOUBLE,
name VARCHAR(255),
url VARCHAR(255),
image_link varchar(255),
FOREIGN KEY (qid) REFERENCES queries(id),
FOREIGN KEY (sid) REFERENCES sellers(id),
FOREIGN KEY (bid) REFERENCES brands(id));


