/*
 * RELATIONAL DATABASE DEFINITIONS FOR DICTIONARY TABLES
 * ============================================================================
 */

/*
 * Tables for a Chinese to English word dictionary. Tables include grammar,
 *     topics, and words.
 * 
 * Also see files drop.sql and load_data.sql. Create the database 'cse_dict'
 * before executing this file. Use this file by logging into the mysql client
 * and executing the command
 *
 * > source dictionary.ddl
 */

use cse_dict;

/*
 * Table for grammar for Chinese words.
 *
 * Each word in the words table should have an entry that matches a record
 * in the grammar table.
 */
CREATE TABLE grammar (english VARCHAR(125) NOT NULL,
                      PRIMARY KEY (english)
                     )
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

/*
 * Table for topics
 *
 * Words can be classified into topics. This helps the user know the context within
 * which a word is used.
 *
 * simplified:  Simplified Chinese text describing the topic
 * english:     English text describing the topic
 * url:	        The URL of a page to display information about the topic
 * title:       The title of the page to display information about the topic
 */
CREATE TABLE topics (simplified VARCHAR(125) NOT NULL,
                     english VARCHAR(125) NOT NULL,
                     url VARCHAR(125),
                     title TEXT,
                     PRIMARY KEY (simplified, english)
                    )
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

/*
 * Table for Chinese to English mapping of words
 *
 * Each entry in the table represents one sense of a Chinese word.
 *
 * id           A unique identifier for the word
 * simplified:	Simplified Chinese text for the word
 * traditional:	Traditional Chinese text for the word (if different)
 * pinyin:      Hanyu pinyin
 * english:     English text for the word 
 * function:	Grammatical function 
 * concept_cn:	The general concept for the word in Chinese (country, chemical, etc)
 * concept_en:	The general concept for the word in English (country, chemical, etc)
 * topic_cn:	The general topic for the word in Chinese (geography, technology, etc)
 * topic_en:	The general topic for the word in English (geography, technology, etc)
 * parent_cn:	The parent for the concept (Chinese)
 * parent_en:	The parent for the concept (English)
 * mp3:         Name of an audio file for the word
 * image:       The name of a file for an image illustrating the concept
 * notes:       Notes about the word
 */
CREATE TABLE words (id INT UNSIGNED NOT NULL,
                    simplified VARCHAR(255) NOT NULL,
                    traditional VARCHAR(255),
                    pinyin VARCHAR(255) NOT NULL,
                    english VARCHAR(255) NOT NULL,
                    grammar VARCHAR(255),
                    concept_cn VARCHAR(255),
                    concept_en VARCHAR(255),
                    topic_cn VARCHAR(125),
                    topic_en VARCHAR(125),
                    parent_cn VARCHAR(255),
                    parent_en VARCHAR(255),
                    image VARCHAR(255),
                    mp3 VARCHAR(255),
                    notes TEXT,
                    headword INT UNSIGNED NOT NULL,
                    PRIMARY KEY (id),
                    FOREIGN KEY (topic_cn, topic_en) REFERENCES topics(simplified, english),
                    FOREIGN KEY (grammar) REFERENCES grammar(english),
                    INDEX (simplified),
                    INDEX (traditional),
                    INDEX (english)
    )
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
    ;

/*
 * Table for illustration licenses
 *
 * name:              The type of license
 * license_full_name: The unabbreviated name of the license
 * license_url:	      The URL of the license
 */
CREATE TABLE licenses (name VARCHAR(255) NOT NULL,
                       license_full_name VARCHAR(255) NOT NULL,
                       license_url VARCHAR(255),
                       PRIMARY KEY (name)
                      )
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

/*
 * Table for illustration authors
 *
 * name:        The name of the creator of the image
 * author_url:	The URL of the home page of the creator of the image
 */
CREATE TABLE authors (name VARCHAR(255),
                      author_url VARCHAR(255),
                      PRIMARY KEY (name)
                     )
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

/*
 * Table for illustrations
 *
 * medium_resolution: The file name of a medium resolution image
 * title_zh_cn:       A title in simplified Chinese
 * title_en:          A title in English
 * author:            The creator of the illustration
 * license:           The type of license
 * high_resolution:   The file name of a high resolution image
 */
CREATE TABLE illustrations (medium_resolution VARCHAR(255),
                            title_zh_cn VARCHAR(255) NOT NULL,
                            title_en VARCHAR(255) NOT NULL,
                            author VARCHAR(255),
                            license VARCHAR(255) NOT NULL,
                            high_resolution VARCHAR(255),
                            PRIMARY KEY (medium_resolution),
                            FOREIGN KEY (author) REFERENCES authors(name),
                            FOREIGN KEY (license) REFERENCES licenses(name)
                           )
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

/*
 * Table for unigram frequency.
 *
 * This table records the frequency for the word sense of single words in the 
 * tagged corpus. The Penn Treebank syntax is used for part-of-speech tags.
 *
 * pos_tagged_text: The element text with POS tag and gloss in pinyin and English
 * element_text:    The element text in traditional Chinese
 * word_id:         Matching id in the word table (positive integer)
 * frequency:       The frequency of occurence of the word sense (positive integer)
 */
CREATE TABLE unigram (
	pos_tagged_text VARCHAR(125) NOT NULL,
	element_text VARCHAR(125) NOT NULL,
	word_id INT UNSIGNED NOT NULL,
	frequency INT UNSIGNED NOT NULL,
	PRIMARY KEY (pos_tagged_text),
	FOREIGN KEY (word_id) REFERENCES words(id)
	)
	CHARACTER SET UTF8
	COLLATE utf8_general_ci
;

/*
 * Table for bigram frequency.
 *
 * This table records the frequency for the word sense of sequences of two words 
 * in the tagged corpus.
 *
 * pos_tagged_text: The element text with POS tag and gloss in pinyin and English
 * previous_text:    The element text in traditional Chinese
 * element_text:    The element text in traditional Chinese
 * word_id:         Matching id in the word table (positive integer)
 * frequency:       The frequency of occurence of the word sense (positive integer)
 */
CREATE TABLE bigram (
        id MEDIUMINT NOT NULL AUTO_INCREMENT,
	pos_tagged_text TEXT,
	previous_text VARCHAR(125),
	element_text VARCHAR(125),
	word_id INT UNSIGNED,
	frequency INT UNSIGNED,
	PRIMARY KEY (id),
	FOREIGN KEY (word_id) REFERENCES words(id)
	)
	CHARACTER SET UTF8
	COLLATE utf8_general_ci
;

/*
 * Table for font names
 * font_name_en	The name of the font that the character is rendered in (English)
 * font_name_zh	The name of the font that the character is rendered in (Chinese)
 */
CREATE TABLE font_names (
	font_name_en VARCHAR(80) NOT NULL,
	font_name_zh VARCHAR(80) NOT NULL,
	PRIMARY KEY (font_name_en)
	)
	CHARACTER SET UTF8
	COLLATE utf8_general_ci
;
