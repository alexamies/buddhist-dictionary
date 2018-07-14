import codecs
import fnmatch
import os

with codecs.open('temp.txt', 'w', "utf-8") as f:
  files = sorted(os.listdir('corpus/taisho'))
  for file in files:
    if fnmatch.fnmatch(file, 't*.csv'):
      line = "LOAD DATA LOCAL INFILE 'corpus/%s' INTO TABLE document " \
             "CHARACTER SET utf8 LINES TERMINATED BY '\\n' IGNORE 1 " \
             "LINES;\n" % file
      f.write(line)
