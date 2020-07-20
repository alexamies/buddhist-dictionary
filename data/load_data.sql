USE ntireader;

LOAD DATA LOCAL INFILE 'data/dictionary/grammar.txt' INTO TABLE grammar CHARACTER SET utf8mb4 LINES TERMINATED BY '\r\n';
LOAD DATA LOCAL INFILE 'data/dictionary/topics.txt' INTO TABLE topics CHARACTER SET utf8mb4 LINES TERMINATED BY '\r\n';
LOAD DATA LOCAL INFILE 'data/dictionary/words.txt' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n' IGNORE 1 LINES;
LOAD DATA LOCAL INFILE 'data/dictionary/fgs_mwe.txt' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE 'data/dictionary/buddhist_named_entities.txt' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n' IGNORE 1 LINES;;
LOAD DATA LOCAL INFILE 'data/dictionary/translation_memory_buddhist.txt' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n' IGNORE 1 LINES;;
LOAD DATA LOCAL INFILE 'data/dictionary/translation_memory_literary.txt' INTO TABLE words CHARACTER SET utf8mb4 LINES TERMINATED BY '\n' IGNORE 1 LINES;;
LOAD DATA LOCAL INFILE 'data/dictionary/licenses.txt' INTO TABLE licenses CHARACTER SET utf8mb4 LINES TERMINATED BY '\r\n' IGNORE 1 LINES;;
LOAD DATA LOCAL INFILE 'data/dictionary/authors.txt' INTO TABLE authors CHARACTER SET utf8mb4 LINES TERMINATED BY '\r\n' IGNORE 1 LINES;;
LOAD DATA LOCAL INFILE 'data/dictionary/illustrations.txt' INTO TABLE illustrations CHARACTER SET utf8mb4 LINES TERMINATED BY '\r\n' IGNORE 1 LINES;;
SHOW WARNINGS;
