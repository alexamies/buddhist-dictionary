# -*- coding: utf-8 -*-
"""
Tests utilities for curation of dictionary entries
"""

import cccedict


def TestOpenDictionary():
  cedict = cccedict.OpenDictionary()
  trad = u"日曆"
  if trad not in cedict:
    print u"TestOpenDictionary, %s is not in the dictionary" % trad
  else:
    entry = cedict[u"日曆"]
    print u"TestOpenDictionary, Entry for : %s" % trad
    print u"TestOpenDictionary, Simplified: %s" % entry["simplified"]
    print u"TestOpenDictionary, Pinyin: %s" % entry["pinyin"]
    print u"TestOpenDictionary, English: %s" % entry["english"]


def main():
  print u"test_cccedict"
  TestOpenDictionary()


if __name__ == "__main__": main()