## DICTIONARY DATABASE README
===============================================================================
These instructions are for setting the dictionary data with MySQL. The database 
is needed by the PHP web interface. The Python command line tools do not need a 
database. They work directly from the text files.

1. Install MySQL or use one provided by a hosting company.

2. Set the password for the database. Use the same password in $DICT_HOME/web/inc/database_utils.php.

3. On the command line change to the $DICT_HOME/data/dictionary directory. Log into 
   the mysql client with the command

   $ mysql --local-infile=1 -h localhost -u root -p

   Create a database with the command

   > create database cse_dict;

   The database must be set to a UTF8 character set.

4. Define the database tables. Log into the mysql command line client and run
   DDL commands in dictionary.ddl.

   > source dictionary.ddl

5. Load the data into the tables. Execute this command.

   > source load_data.sql

   Log out of the mysql client.


## TROUBLESHOOTING
===============================================================================
1. When cleaning up data it is good try reload the data cleanly after fixing the
   problems by editing the data files. If you want to reload the data then the 
   drop table statements will help you delete the old data. To drop the tables 
   use the command

> source drop.sql

2. Foreign key problems when loading data.
   MySQL is poor on informing you which rows have foreign key violations.
   However, it prevents you from doing the entire load operation.
   If additional data is added to the tables and not formatted properly then
   you might have this problem.

   If you have errors about foreign keys, then drop the tables and disable the 
   foreign key constraints with this command:

   > SET foreign_key_checks = 0;

   Load the data. Look for the foreign key problem with a select statement.
   For the Sanskrit table use a statement like

   > SELECT id FROM sanskrit WHERE grammar NOT IN (SELECT id FROM sans_grammar);

   For the character table use a statement like

   > SELECT unicode FROM characters WHERE type NOT IN (SELECT type FROM character_types);

   For the variants table use statements like

   > SELECT c1 FROM variants WHERE c1 NOT IN (SELECT c FROM characters);
   > SELECT c2 FROM variants WHERE c2 NOT IN (SELECT c FROM characters);

   For the illustrations table use statements like

   > SELECT medium_resolution, author FROM illustrations WHERE author NOT IN (SELECT name FROM authors);
   > SELECT medium_resolution, license FROM illustrations WHERE license NOT IN (SELECT name FROM licenses);

   Fix the problems by editing the data text file then set the relational check on with

   > SET foreign_key_checks = 1;

   Finally, reload the data.

3. Python and Mysql do not handle some new unicode characters well. For example, it complains about the
   Chinese character with Unicode value 151681. These are mostly archaic characters. These
   characters usually have four bytes, as opposed to most Chinese characters, which have three.
   You will typically get a message from mysql like

   Incorrect string value: '\xF0\xA1\xBB\x95'

   Python 3 may be better but NLTK does not support Python 3 yet. Font support for these new 
   characters is spotty as well and they may easily be corrupted with cut-and-paste.

