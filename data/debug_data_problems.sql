USE ntireader;

/* Number of lexical units. */
select count(*) from words;

/* Word with highest id. */
SELECT
  max(id) as max_id
FROM
  words;

/* Word with specific id. */
SELECT
  id
FROM
  words
WHERE
  id = 107129;

/* Disable referential integrity*/
SET @@foreign_key_checks = 0;

/* Enable referential integrity*/
SET @@foreign_key_checks = 1;

/* Load rejected words. */
LOAD DATA LOCAL INFILE 'rejected.tsv' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n' IGNORE 1 LINES;
show warnings;

/* Find words with topics that do not match*/
SELECT
  id, topic_cn
FROM
  words
WHERE
  id NOT in (
  SELECT
    simplified
  FROM
    topics
  )
LIMIT 20;