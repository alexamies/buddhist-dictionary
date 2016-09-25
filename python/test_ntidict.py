# -*- coding: utf-8 -*-
"""
Tests utilities for curation of dictionary entries
"""

import ntidict


def TestOpenDictionary():
  wdict = ntidict.OpenDictionary()
  entry = wdict[u"日曆"]
  print u"TestOpenDictionary, English: %s" % entry["english"]


def main():
  TestOpenDictionary()


if __name__ == "__main__": main()