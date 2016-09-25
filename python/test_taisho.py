# -*- coding: utf-8 -*-
"""
Tests utility for Korean canon metadata management
"""

import codecs

import taisho


def main():
  #saveScrollFromWeb(14, "541", 1, u"佛說佛大僧大經")
  #saveScrolls(14, "542", 1, u"佛說耶祇經")
  #saveScrolls(14, "543", 3, u"佛說巨力長者所問大乘經")
  taisho.saveScrolls(16, "686", 1, u"佛說報恩奉盆經")


if __name__ == "__main__": main()