# -*- coding: utf-8 -*-

# Check bigrams for presence in Chinese Wikipedia

import codecs

from char_util import ToSimplified


def get_pinyin_unaccented(pinyin_numbers):
  pinyin = []
  for syllable in delimiter_pattern.split(pinyin_numbers):
    pinyin.append(syllable)
  return (" ").join(pinyin).strip()


def get_wiki_headwords():
  headwords = []
  with codecs.open("zhwiki_hw_trad.txt", "rt", "utf-8") as zhwiki:
    for hw in zhwiki:
      headwords.append(hw.strip())
  print("get_wiki_headwords: found %d wikipedia headwords" % len(headwords))
  return set(headwords)


def main():
  print "Looking for bigrams that are entries in wikipedia"
  luid = 76969
  mutual_bigram_info = {}
  temp_dict = {}
  with codecs.open('../../hsingyundl/index/ngram_frequencies.txt', 'rt', "utf-8") as bigram_file:
    wiki_hw = get_wiki_headwords()
    with codecs.open("temp.tsv", "w", "utf-8") as f:
      for line in bigram_file:
        info = line.split()
        if info[0] in wiki_hw:
          luid += 1
          traditional = info[0]
          simplified, trad, pinyin = ToSimplified(traditional)
          english = u"English"
          grammar = u"noun"
          concept = u"\\N\t\\N"
          domain = u"现代汉语\tModern Chinese"
          subdomain = u"\\N\t\\N"
          notes = u"(Wikipedia '{0}')".format(simplified)
          f.write(u"{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t\\N\t\\N\t{9}\t{10}\n".format(luid,
          	simplified, trad, pinyin, english, grammar, concept, domain, subdomain, notes, luid))


if __name__ == "__main__":
  main()
