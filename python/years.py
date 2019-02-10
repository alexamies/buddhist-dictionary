# -*- coding: utf-8 -*-

# Add years between 1900年 and 2020年 in Chinese numerals

import codecs

from ntidict import OpenDictionary
from char_util import ToSimplified

chinese = {0: u'〇', 1: u'一', 2: u'二', 3: u'三', 4: u'四', 5: u'五', 6: u'六',
           7: u'七', 8: u'八', 9: u'九'}

def main():
  print "main enter"
  ntidict = OpenDictionary()
  luid = 93386
  trad = u"\\N"
  grammar = "number"
  concept = u"\\N\t\\N"
  domain = u"现代汉语\tModern Chinese"
  subdomain = u"数量\tQuantity"
  with codecs.open("numbers.tsv", "w", "utf-8") as f:
    for n in range(1900, 2021):
      d1 = n / 1000
      d2 = (n - d1 * 1000) / 100
      d3 = (n - d1 * 1000 - d2 * 100) / 10
      d4 = (n - d1 * 1000 - d2 * 100 - d3 * 10) / 1
      c = chinese[d1] + chinese[d2] + chinese[d3] + chinese[d4] + u"年"
      #print(u"%d: %s" % (n, c))
      if c not in ntidict:
      	#print(u"%s is not in dict" % c)
      	luid += 1
        _, _, p1 = ToSimplified(chinese[d1] + chinese[d2] + chinese[d3] + chinese[d4])
        pinyin = p1 + u" nián"
        notes = u"(Wikipedia '%d年')" % n
        f.write(u"{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t\\N\t\\N\t{9}\t{10}\n".format(luid,
            c, trad, pinyin, n, grammar, concept, domain, subdomain, notes, luid))


if __name__ == "__main__":
  main()
