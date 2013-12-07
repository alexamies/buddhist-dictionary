/*
 * RELATIONAL DATABASE DEFINITIONS FOR DICTIONARY TABLES
 * ============================================================================
 */

/*
 * There are three dictionaries and related tables:
 *
 * words: A Chinese to English word dictionary (not here yet)
 *
 * characters: A character dictionary. Includes tables characters. Includes
 *     tables characters, character_types, character_rend.txt, and radicals. 
 *     This table only
 *     has a small number of characters (3425) at the moment. It is not 
 *     large enough for a dictionary of Chinese characters but it is used by
 *     some web pages explaining Chinese radicals, fonts, Sanskrit, and IPA.
 *
 * sanskrit: A Sanskrit to Chinese dictionary with English meanings added.
 *     Includes tables sans_grammar and sanskrit.
 *
 * The text files in the same directory map one-to-one to the table names.
 * 
 * Also see files drop.sql and load_data.sql. Create the database 'cse_dict'
 * before executing this file. Use this file by logging into the mysql client
 * and executing the command
 *
 * > source dictionary.ddl
 */

use cse_dict;


/*
 * Table for Kangxi radicals
 *
 * id           A unique identifier for the radical
 * traditional  Traditional Chinese text for the radical
 * simplified   Simplified Chinese text for the radical (if different)
 * pinyin       Hanyu pinyin
 * strokes      The number of strokes
 * other_forms  Other forms of the radical
 * english      English text for the radical 
 */
CREATE TABLE radicals (id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                       traditional VARCHAR(10) NOT NULL,
                       simplified VARCHAR(10),
                       pinyin VARCHAR(10),
                       strokes INT UNSIGNED NOT NULL,
                       simplified_strokes INT UNSIGNED,
                       other_forms VARCHAR(255),
                       english VARCHAR(255) NOT NULL,
                       PRIMARY KEY (id),
                       INDEX (traditional)
                      )
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

/*
 * Types of characters. For example, Sanskrit, traditional Chinese, IPA.
 * 
 * type   A key for the type name
 * name   An English name for the type
 */
CREATE TABLE character_types (
	type VARCHAR(125) NOT NULL,
	name VARCHAR(125) NOT NULL,
	PRIMARY KEY (type)
	)
	CHARACTER SET UTF8
	COLLATE utf8_general_ci
;

/*
 * Table for character dictionary.
 * 
 * Table maps characters to English meaning with Unicode codes as primary key. 
 * Most entries are Chinese characters. There are fields for number of strokes and pronuncia
 *
 * unicode        The Unicode unique identifier for the character (decimal)
 * c              Chinese text for the character (simplified, traditional, or other symbol)
 * pinyin         Hanyu pinyin
 * radical        Main radical
 * strokes        The number of strokes
 * other_strokes  The number of strokes other than the main radical
 * english        English text for the radical 
 * notes:         Miscellaneous notes about the character, if any
 */
CREATE TABLE characters (unicode INT UNSIGNED NOT NULL,
                         c VARCHAR(10) NOT NULL,
                         pinyin VARCHAR(80),
                         radical VARCHAR(10),
                         strokes INT UNSIGNED NOT NULL,
                         other_strokes INT UNSIGNED NOT NULL,
                         english VARCHAR(255) NOT NULL,
                         notes TEXT,
                         type VARCHAR(125) NOT NULL,
                         hangul VARCHAR(10),
                         PRIMARY KEY (unicode),
                         FOREIGN KEY (type) REFERENCES character_types(type),
                         UNIQUE (c),
                         INDEX (c)
                        )
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

/*
 * Table for relationship between character variants, traditional / simplified and other variant
 * c1             The UTF-8 text for the subject character
 * c2:            The UTF-8 text for the variant character
 * relation_type: Traditional / simplified or other variant
 */
CREATE TABLE variants (
	c1 VARCHAR(10) NOT NULL,
	c2 VARCHAR(10) NOT NULL,
	relation_type VARCHAR(255) NOT NULL,
	PRIMARY KEY (c1,c2),
	FOREIGN KEY (c1) REFERENCES characters(c),
	FOREIGN KEY (c2) REFERENCES characters(c),
	INDEX (c1),
	INDEX (c2)
	)
	CHARACTER SET UTF8
	COLLATE utf8_general_ci
;

/*
 * Table for Sanskrit grammar
 *
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
 * Table for Sanskrit word dictionary
 *
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

