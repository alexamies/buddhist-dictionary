/*
 * RELATIONAL DATABASE DEFINITIONS FOR Document Search
 * ============================================================================
 */

/*
 * Tables for corpus metadata and index
 *
 * Execute from same directory:
 * > source hbreader.ddl
 */
USE ntireader;

/*
 * Table for collection titles
 */
CREATE TABLE collection (
	collection_file VARCHAR(256) NOT NULL,
    gloss_file VARCHAR(256) NOT NULL,
	title mediumtext NOT NULL,
	description mediumtext NOT NULL,
	intro_file VARCHAR(256) NOT NULL,
	corpus_name VARCHAR(256) NOT NULL,
	format VARCHAR(256),
    period VARCHAR(256),
    genre VARCHAR(256)
	)
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

/*
 * Table for document titles
 */
CREATE TABLE document (
	source_file VARCHAR(256) NOT NULL,
    gloss_file VARCHAR(256) NOT NULL,
	title mediumtext NOT NULL
	)
    CHARACTER SET UTF8
    COLLATE utf8_general_ci
;

/*
 * Table for word frequencies in documents
 * word - Chinese text for the word
 * frequency - the count of words in the document
 * document - the filename of the HTML Chinese text document
 * idf - inverse document frequency log[(M + 1) / df(w)]
 */
CREATE TABLE word_freq_doc (
  word VARCHAR(256) NOT NULL,
  frequency INT UNSIGNED NOT NULL,
  document VARCHAR(256) NOT NULL,
  idf FLOAT NOT NULL,
  PRIMARY KEY (`word`, `document`)
  )
  CHARACTER SET UTF8
  COLLATE utf8_general_ci
;
