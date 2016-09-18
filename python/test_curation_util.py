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
  (v, tid, nscrolls, translator, dynasty) = ExtractFromColophon(colophon_cn)
  print "TestExtractFromColophon1"
  print "Returned volume %d" % v
  print u"Returned nscrolls %d" % nscrolls
  print u"Returned translator %s" % translator
  print u"Returned dynasty %s\n" % dynasty


def TestExtractFromColophon2():
  colophon_cn = u"""第 14 冊　No. 0489

佛說除蓋障菩薩所問經
宋 法護等譯

共 20 卷"""
  (v, tid, nscrolls, translator, dynasty) = ExtractFromColophon(colophon_cn)
  print "TestExtractFromColophon2"
  print "Returned volume %d" % v
  print "Returned tid '%s'" % tid
  print u"Returned nscrolls %d" % nscrolls
  print u"Returned translator '%s'" % translator
  print u"Returned dynasty '%s'" % dynasty


def TestExtractFromColophon3():
  colophon_cn = u"""第 14 冊　No. 0446a

過去莊嚴劫千佛名經
闕譯

共 1 卷"""
  (v, tid, nscrolls, translator, dynasty) = ExtractFromColophon(colophon_cn)
  print "TestExtractFromColophon3"
  print "Returned volume %d" % v
  print u"Returned nscrolls %d" % nscrolls
  print u"Returned translator %s" % translator
  print u"Returned dynasty %s" % dynasty


def TestExtractFromColophon4():
  colophon_cn = u"""第 14 冊　No. 0493

佛說阿難四事經
吳 支謙譯

共 1 卷"""
  (v, tid, nscrolls, translator, dynasty) = ExtractFromColophon(colophon_cn)
  print "TestExtractFromColophon4"
  print "Returned volume %d" % v
  print "Returned tid '%s'" % tid
  print u"Returned nscrolls %d" % nscrolls
  print u"Returned translator %s" % translator
  print u"Returned dynasty %s" % dynasty


def TestExtractFromColophon5():
  colophon_cn = u"""第 14 冊　No. 0492a

佛說阿難問事佛吉凶經
後漢 安世高譯

共 1 卷"""
  (v, tid, nscrolls, translator, dynasty) = ExtractFromColophon(colophon_cn)
  print "TestExtractFromColophon5"
  print "Returned volume %d" % v
  print "Returned tid '%s'" % tid
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
  #TestExtractFromColophon2()
  #TestExtractFromColophon3()
  TestExtractFromColophon4()
  TestExtractFromColophon5()


if __name__ == "__main__": main()