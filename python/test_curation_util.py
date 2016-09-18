# -*- coding: utf-8 -*-
"""
Tests utilities for curation of dictionary entries
"""
from curation_util import ExtractFromColophon
from curation_util import ExtractWords
from curation_util import P2englishPN
from curation_util import WriteColophon

def TestExtractFromColophon1():
  colophon_cn = u"""第 14 冊　No. 0442

十方千五百佛名經
失譯

共 1 卷"""
  (v, nscrolls, translator, dynasty) = ExtractFromColophon(colophon_cn)
  print "TestExtractFromColophon1"
  print "Returned volume %d" % v
  print u"Returned nscrolls %d" % nscrolls
  print u"Returned translator %s" % translator
  print u"Returned dynasty %s\n" % dynasty


def TestExtractFromColophon2():
  colophon_cn = u"""第 14 冊　No. 0470

佛說文殊師利巡行經
元魏 菩提流支譯

共 1 卷"""
  (v, nscrolls, translator, dynasty) = ExtractFromColophon(colophon_cn)
  print "TestExtractFromColophon2"
  print "Returned volume %d" % v
  print u"Returned nscrolls %d" % nscrolls
  print u"Returned translator '%s'" % translator
  print u"Returned dynasty '%s'" % dynasty


def TestExtractFromColophon3():
  colophon_cn = u"""第 14 冊　No. 0446a

過去莊嚴劫千佛名經
闕譯

共 1 卷"""
  (v, nscrolls, translator, dynasty) = ExtractFromColophon(colophon_cn)
  print "TestExtractFromColophon3"
  print "Returned volume %d" % v
  print u"Returned nscrolls %d" % nscrolls
  print u"Returned translator %s" % translator
  print u"Returned dynasty %s" % dynasty


def TestExtractFromColophon4():
  colophon_cn = u"""第 14 冊　No. 0447b

現在賢劫千佛名經
共 1 卷"""
  (v, nscrolls, translator, dynasty) = ExtractFromColophon(colophon_cn)
  print "TestExtractFromColophon4"
  print "Returned volume %d" % v
  print u"Returned nscrolls %d" % nscrolls
  print u"Returned translator %s" % translator
  print u"Returned dynasty %s" % dynasty


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
  #TestExtractFromColophon1()
  TestExtractFromColophon2()
  #TestExtractFromColophon3()
  #TestExtractFromColophon4()


if __name__ == "__main__": main()