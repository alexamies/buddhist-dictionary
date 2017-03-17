# -*- coding: utf-8 -*-
"""
Does term extraction on the NTI Reader corpus

Compares bigrams from corpus against headwords in other dictionaries.
"""
import codecs


NGRAM_FILE_NAME = '../index/ngram_frequencies.txt'
DINGFUBAO_FILE_NAME = 'dingfubao.txt'
NEWWORDS_FILE_NAME = 'newwords.txt'
PROCESS_MAX = 10000000


def check_ngrams(dingfubao):
  i = 0
  with codecs.open(NGRAM_FILE_NAME, 'r', "utf-8") as f:
    with codecs.open(NEWWORDS_FILE_NAME, 'w', "utf-8") as g:
      for line in f:
        if i >= PROCESS_MAX:
          break
        i += 1
        line = line.strip()
        if not line:
          continue
        fields = line.split('\t')
        if fields and len(fields) >= 1:
          ngram = fields[0]
          if ngram in dingfubao:
          	g.write(ngram + '\n')


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


def main():
  dingfubao = load_headwords(DINGFUBAO_FILE_NAME)
  print "Ding Fubao: ", len(dingfubao)
  check_ngrams(dingfubao)


if __name__ == "__main__":
  main()