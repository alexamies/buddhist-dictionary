/*
 * RELATIONAL DATABASE DROP STATEMENTS
 * ============================================================================
 */

/*
 * These drop statements will drop the database tables deleting the data in the
 * process. Be careful!
 * 
 * Use this file by logging into the mysql client and executing the command
 *
 * > source dictionary.ddl
 */

use cse_dict;

drop table sanskrit;
drop table sans_grammar;
drop table characters;
drop table character_types;
drop table radicals
