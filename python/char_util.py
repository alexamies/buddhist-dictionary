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
      simplified += entry['simplified']
      pinyin += entry['pinyin']
    else:
      simplified += t
      pinyin += ' '
  if simplified == trad:
    traditional = "\\N"
  return simplified, traditional, pinyin.lower()


def ToTraditional(chinese):
  traditional = u""
  for c in chinese:
    if c in cedict:
      entry = cedict[c]
      s = entry['simplified']
      t = entry['traditional']
      if t ==  "\\N":
        t = s
      traditional += t
  return traditional

# Basic test
def main():
  print("Test ToSimplified()")
  trad = u"四種廣說"
  s, t, p = ToSimplified(trad)
  print(u"%s %s %s" % (s, t, p))

  print("Test ToTraditional()")
  chinese = u"操作系统"
  traditional = ToTraditional(chinese)
  print(u"%s" % traditional)



if __name__ == "__main__":
  main()