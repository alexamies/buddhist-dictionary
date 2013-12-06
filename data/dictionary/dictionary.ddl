/*
 * Before the first time you run this create the database:
 * create database cse_dict;
 */
use cse_dict;

drop table sanskrit;
drop table sans_grammar;

/*
 * Table for Sanskrit grammar
 * id			A unique identifier for the grammatical type
 * name:		The full name of the grammatical type
 * notes:		More information
 */
CREATE TABLE sans_grammar (id VARCHAR(255) NOT NULL,
                           name VARCHAR(255) NOT NULL,
                           notes TEXT,
                           PRIMARY KEY (id)
                          )
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

/*
 * Table for Sanskrit words
 * id			A unique identifier for the word
 * word_id:		The id in the Chinese word table
 * latin		The Latin text for the word
 * iast:		The International Alphabet for Sanskrit Transliteration accented text
 * devan:		The Devanagari text for the word
 * pali:		The Pali text for the word
 * traditional:	The traditional Chinese text for the word
 * english: 	The English text for the word
 * notes: 		General notes
 * grammar: 	The grammatical type
 */
CREATE TABLE sanskrit (id INT UNSIGNED NOT NULL,
                       word_id INT UNSIGNED NOT NULL,
                       latin VARCHAR(255) NOT NULL,
                       iast VARCHAR(255),
                       devan VARCHAR(255),
                       pali VARCHAR(255),
                       traditional VARCHAR(255) NOT NULL,
                       english VARCHAR(255) NOT NULL,
                       notes TEXT,
                       grammar VARCHAR(255),
                       root VARCHAR(255),
                       PRIMARY KEY (id),
                       /* FOREIGN KEY (word_id) REFERENCES words(id),*/
                       FOREIGN KEY (grammar) REFERENCES sans_grammar(id)
                      )
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

