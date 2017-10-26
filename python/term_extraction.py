# -*- coding: utf-8 -*-
"""
Does term extraction on the NTI Reader corpus

Compares bigrams from corpus against headwords in other dictionaries.
"""
import codecs

from char_util import ToSimplified

NGRAM_FILE_NAME = '../../hsingyundl/index/ngram_frequencies.txt'
DINGFUBAO_FILE_NAME = 'dingfubao.txt'
NEWWORDS_FILE_NAME = '../../hsingyundl/index/newdingwords.txt'
NEWWORDS_TSV_FILE = '../../hsingyundl/index/newdingwords.tsv'
PROCESS_MAX = 1000000


def check_ngrams(dingfubao):
  i = 0
  with codecs.open(NGRAM_FILE_NAME, 'r', "utf-8") as f:
    with codecs.open(NEWWORDS_FILE_NAME, 'w', "utf-8") as g:
      g.write('Traditional\tOccurences\n')
      for line in f:
        if i >= PROCESS_MAX:
          break
        i += 1
        line = line.strip()
        if not line:
          continue
        fields = line.split('\t')
        if fields and len(fields) >= 2:
          ngram = fields[0]
          freq = fields[1]
          if ngram in dingfubao:
          	entry = "%s\t%s\n" % (ngram, freq)
          	g.write(entry)


def load_headwords(filename):
  headwords = []
  with codecs.open(DINGFUBAO_FILE_NAME, 'r', "utf-8") as f:
    for line in f:
      if line.startswith('#'):
        print "Loading: ", line
      else:
        hw = line.strip()
        headwords.append(hw)
  return set(headwords)


def write_words(dingfubao):
  i = 0
  j = 0
  luid = 68062
  with codecs.open(NGRAM_FILE_NAME, 'r', "utf-8") as f:
    with codecs.open(NEWWORDS_TSV_FILE, 'w', "utf-8") as g:
      for line in f:
        if i >= PROCESS_MAX:
          break
        i += 1
        line = line.strip()
        if not line:
          continue
        fields = line.split('\t')
        ngram = fields[0]
        if ngram in dingfubao:
          luid += 1
          traditional = fields[0]
          simplified, trad, pinyin = ToSimplified(traditional)
          english = ""
          grammar = "set phrase"
          concept = u"\\N\t\\N"
          domain = u"佛教\tBuddhism"
          g.write(u"{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t\\N\t\\N\t\\N\t\\N\t(Ding '{8}')\t{9}\n".format(luid,
              simplified, trad, pinyin, english, grammar, concept, domain, traditional, luid))
        else:
          #print "Did not match %s" % ngram
          j += 1
  print "processed %d entries, %d did not match" % (i, j)


def main():
  dingfubao = load_headwords(DINGFUBAO_FILE_NAME)
  print "Ding Fubao: ", len(dingfubao)
  #check_ngrams(dingfubao)
  write_words(dingfubao)


if __name__ == "__main__":
  main()