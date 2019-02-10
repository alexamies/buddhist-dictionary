# -*- coding: utf-8 -*-

# Check Chinese integers below 100

import codecs

from ntidict import OpenDictionary
from char_util import ToSimplified

chinese = {0: u'〇', 1: u'一', 2: u'二', 3: u'三', 4: u'四', 5: u'五', 6: u'六',
           7: u'七', 8: u'八', 9: u'九'}

def main():
  print "main enter"
  ntidict = OpenDictionary()
  luid = 93333
  trad = u"\\N"
  grammar = "number"
  concept = u"\\N\t\\N"
  domain = u"现代汉语\tModern Chinese"
  subdomain = u"数量\tQuantity"
  with codecs.open("numbers.tsv", "w", "utf-8") as f:
    for n in range(20, 100):
      c = chinese[n / 10] + u'十'
      if n % 10 != 0:
        c += chinese[n % 10]
      #print(u"%d: %s" % (n, c))
      if c not in ntidict:
      	#print(u"%s is not in dict" % c)
      	luid += 1
        _, _, pinyin = ToSimplified(c)
        notes = u"(Wikipedia '%d')" % n
        f.write(u"{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t\\N\t\\N\t{9}\t{10}\n".format(luid,
            c, trad, pinyin, n, grammar, concept, domain, subdomain, notes, luid))


if __name__ == "__main__":
  main()
