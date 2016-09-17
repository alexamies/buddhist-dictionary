# -*- coding: utf-8 -*-
"""
Tests utilities for curation of dictionary entries
"""
from curation_util import ExtractFromColophon
from curation_util import ExtractWords
from curation_util import P2englishPN
from curation_util import WriteColophon

def TestExtractFromColophon():
  colophon_cn = u"""第 14 冊　No. 0442

十方千五百佛名經
失譯

共 1 卷"""
  (v, t, nscrolls) = ExtractFromColophon(colophon_cn)
  print "Returned volume %d" % v
  print u"Returned translator %s" % t
  print u"Returned nscrolls %d" % nscrolls


def TextExtractWords(text):
  words = ExtractWords(text)
  print "result"
  for w in words:
    print u"  Word: %s" % w.decode("utf-8")


def main():
  #print P2englishPN(u"guān Xūkōng Zàng Púsà jīng")
  #TextExtractWords(u"你好世界")
  #TextExtractWords(u"你好美國")
  #TextExtractWords(u"经")
  #WriteColophon(0, "", 0, "", "", "")
  TestExtractFromColophon()


if __name__ == "__main__": main()