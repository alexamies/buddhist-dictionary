# -*- coding: utf-8 -*-
"""
Tests utility for Korean canon metadata management
"""

import codecs

from taisho import htmlToPlainText
from taisho import saveScrolls
from taisho import saveScrollFromWeb


def testHtmlToPlainText():
  html = u""
  with codecs.open("t0543_001.html", 'r', "utf-8") as f:
  	for line in f:
  	  html += line
  text = htmlToPlainText(html, "0543")
  with codecs.open("test.txt", 'w', "utf-8") as outfile:
    outfile.write(text)

def main():
  #saveScrollFromWeb(14, "541", 1, u"佛說佛大僧大經")
  #saveScrolls(14, "542", 1, u"佛說耶祇經")
  saveScrolls(14, "543", 3, u"佛說巨力長者所問大乘經")
  #testHtmlToPlainText()


if __name__ == "__main__": main()