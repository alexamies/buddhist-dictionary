USE ntireader;

LOAD DATA LOCAL INFILE 'dictionary/grammar.txt' INTO TABLE grammar CHARACTER SET utf8mb4 LINES TERMINATED BY '\r\n';
LOAD DATA LOCAL INFILE 'dictionary/topics.txt' INTO TABLE topics CHARACTER SET utf8mb4 LINES TERMINATED BY '\r\n';
LOAD DATA LOCAL INFILE 'dictionary/words.txt' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'dictionary/fgs_mwe.txt' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE 'dictionary/buddhist_named_entities.txt' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE 'dictionary/translation_memory_buddhist.txt' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE 'dictionary/translation_memory_literary.txt' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE 'dictionary/licenses.txt' INTO TABLE licenses CHARACTER SET utf8mb4 LINES TERMINATED BY '\r\n';
LOAD DATA LOCAL INFILE 'dictionary/authors.txt' INTO TABLE authors CHARACTER SET utf8mb4 LINES TERMINATED BY '\r\n';
LOAD DATA LOCAL INFILE 'dictionary/illustrations.txt' INTO TABLE illustrations CHARACTER SET utf8mb4 LINES TERMINATED BY '\r\n';
SHOW WARNINGS;
