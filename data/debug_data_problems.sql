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

/* Load rejected words. */
LOAD DATA LOCAL INFILE 'rejected.tsv' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n' IGNORE 1 LINES;
show warnings;