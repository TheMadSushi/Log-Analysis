#LOG ANALYSIS

Print report based on data in database using python and postgresql to get information from a newspaper website regarding the most popular author, 
most popular articles and the percentages of error while loading the page

##Installation

*Make sure you have installed python in your computer. You can find instructions to install python [here](http://docs.python-guide.org/en/latest/starting/installation/)
*Make sure you have installed vagrant in your machine. You can find instructions [here] (https://www.vagrantup.com/)
*Make sure you have installed virtual box in your machine. You can find instructions [here](https://www.virtualbox.org/)
*Clone or download fullstack-nandegree-vm repository. You can download it from [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
*Get newsdata.sql in the same folder as that of vagrant. You can download it from [here] (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
*Make sure that the following files are saved in the same folder : 
1. project.py

##Pre-requisites
Install Vagrant and virtual box
Download udacity vagrant directory
Download common code for database as a zip file from here
Step 2 will provide newsdata.sql

##Instructions
* On your terminal start the virtual machine by using 'vagrant up'command
*vagrant ssh to login into vm
* cd /vagrant
*use command psql -d news -f newsdata.sql to load database
-use \c to connect to database="news"
-use \dt to see the tables in database
-use \dv to see the views in database
-use \q to quit the database
*use command python project.py to run the programm
Queries Used to create the view

CREATE OR REPLACE VIEW popular_article_vew AS
SELECT popular_title, COUNT(*) AS views FROM (SELECT CONCAT('/article/', slug) AS short_path, TITLE popular_title FROM articles)
AS pop_articles, log, articles WHERE short_path = path AND articles.title = popular_title GROUP BY
popular_title ORDER BY views DESC LIMIT 3;

CREATE OR REPLACE VIEW popular_author_vew AS
SELECT pop_authors, COUNT(*) AS views FROM log, (SELECT CONCAT('/article/', slug) AS short_path ,authors.name
AS pop_authors FROM articles, authors WHERE articles.author = authors.id) AS foo WHERE short_path = log.path GROUP BY
pop_authors ORDER BY views DESC;

CREATE OR REPLACE VIEW err_log_vew AS
SELECT * FROM (SELECT a.day, ROUND(CAST((100*b.hits) AS NUMERIC) / CAST(a.hits AS NUMERIC), 2)
AS err FROM (SELECT DATE(TIME) AS day, COUNT(*) AS hits FROM log GROUP BY day) AS a INNER JOIN
(SELECT DATE(TIME) AS day, COUNT(*) AS hits FROM log WHERE STATUS LIKE '%404%' GROUP BY day) AS b
ON a.day = b.day) AS foo WHERE err > 1.0;


##License

This is an open source code. 
