DICTIONARY DATABASE README
===============================================================================
These instructions are for setting the dictionary data with MySQL. The database 
is needed by the PHP web interface. The Python command line tools do not need a 
database. They work directly from the text files.

1) Install MySQL or use one provided by a hosting company.

2) Set the password for the database. Use the same password in $DICT_HOME/web/inc/database_utils.php.

3) On the command line change to the $DICT_HOME/data/dictionary directory. Log into 
   the mysql client with the command

   $ mysql --local-infile=1 -h localhost -u root -p

   Create a database with the command

   > create database cse_dict;

   The database must be set to a UTF8 character set.

4) Define the database tables. Log into the mysql command line client and run
   DDL commands in dictionary.ddl.

   > source dictionary.ddl

   If you want to reload the data then the drop table statements will help you
   delete the old data. To drop the tables use the command

   > source drop.sql

5) Load the data into the tables. Execute this command.

   > source load_data.sql

   Log out of the mysql client.


TROUBLESHOOTING
===============================================================================
1. Foreign key problems when loading data.
   MySQL is poor on informing you which rows have foreign key violations.
   However, it prevents you from doing the entire load operation.
   If you have errors about foreign keys, then drop the tables and disable the 
   foreign key constraints with this command:

   > SET foreign_key_checks = 0;

   Load the data. Look for the foreign key problem with a select statement like

   > SELECT id FROM sanskrit WHERE grammar NOT IN (SELECT id FROM sans_grammar);

   Fix the problems then set the relational check on with

   > SET foreign_key_checks = 1;

   Finally, reload the data.

