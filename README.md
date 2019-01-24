# BigData
## pig -useHCatalog
## hive'a uruchamiamy wpisujac hive
## show databases
## use database
## w hive normalny sql, bez jaj
## a = LOAD 'database.table' using org.apache.hive.hcatalog.pig.HCatLoader();
## describe/dump a
## FILTER = WHERE
## STORE student INTO ' hdfs://localhost:9000/pig_Output/ ' USING PigStorage (',');
## verification:
## hdfs dfs -ls 'hdfs://localhost:9000/pig_Output/'
## hdfs dfs -cat 'hdfs://localhost:9000/pig_Output/part-m-00000' 
## trudne jakies:
## student = LOAD 'hdfs://localhost:9000/pig_data/student_data.txt' USING PigStorage(',')
##   as ( id:int, firstname:chararray, lastname:chararray, phone:chararray, city:chararray );
## spark: https://www.tutorialspoint.com/apache_spark/apache_spark_installation.htm
## zeppelin: https://zeppelin.apache.org/docs/0.5.5-incubating/tutorial/tutorial.html
## https://en.blog.businessdecision.com/bigdata-en/2017/04/tutorial-first-steps-with-zeppelin/
## jeszcze coś o pigu: http://guyharrison.squarespace.com/blog/2012/1/6/getting-started-with-apache-pig.html
## zep -=> https://youtu.be/CfhYFqNyjGc?t=223
