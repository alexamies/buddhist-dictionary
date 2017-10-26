# -*- coding: utf-8 -*-
"""
Utility for converting traditional to simplified and Pinyin
"""
from ntidict import OpenDictionary

cedict = OpenDictionary()

def ToSimplified(trad):
  simplified = u""
  traditional = trad
  pinyin = u""
  for t in trad:
    if t in cedict:
      entry = cedict[t]
      s = entry['simplified']
      p = entry['pinyin']
      simplified += s
      pinyin += p
    else:
      s = u"Not found"
      p = u"Not found"
  if simplified == trad:
    traditional = "\\N"
  return simplified, traditional, pinyin.lower()


def main():
  trad = u"四種廣說"
  s, t, p = ToSimplified(trad)
  print u"%s %s %s" % (s, t, p)


if __name__ == "__main__":
  main()