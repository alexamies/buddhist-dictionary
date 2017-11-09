# -*- coding: utf-8 -*-

# Extracts headwords from the Chinese version of Wikipedia

# Source https://dumps.wikimedia.org/backup-index.html
# zhwiki-20171103-pages-articles-multistream-index.txt.bz2

import codecs

from char_util import ToTraditional


# Process a single line
def parse_entry(line):
  tokens = line.split(":")
  hw = tokens[-1]
  return ToTraditional(hw)


def test():
  headwords = []
  with codecs.open("zhwiki_hw_trad.txt", "rt", "utf-8") as zhwiki:
    for hw in zhwiki:
      headwords.append(hw.strip())
  print("test: found %d wikipedia headwords" % len(headwords))
  hw_set = set(headwords)
  word = u"田寮"
  if word in hw_set:
    print("%s is in zhwiki, as expected" % word)
  else:
    print("%s is not in zhwiki, which is not expected" % word)


def main():
  print("main: start")
  headwords = []
  with codecs.open("zhwiki.txt", "rt", "utf-8") as zhwiki:
    for line in zhwiki:
      headword = parse_entry(line)
      headwords.append(headword)
  print("main: found %d headwords" % len(headwords))
  i = 0
  with codecs.open("zhwiki_hw_trad.txt", "w", "utf-8") as f:
    for hw in headwords:
      if len(hw) == 0:
        continue
      i += 1
      if i % 100000 == 0:
        print("main: writing headword %d: %s" % (i, hw))
      f.write(u"{0}\n".format(hw))
  test()

if __name__ == "__main__":
  main()

