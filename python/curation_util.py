# -*- coding: utf-8 -*-
"""
Utility for curation of dictionary entries in the accompanying Jupyter
notebook.
"""
import unicodedata

"""
Takes a pinyin string and returns a string with the diacritics removed and
initial letters capitalized, as a guess for the English proper noun.
"""
def p2englishPN(pinyin):
  english = u""
  parts = pinyin.split(" ")
  for part in parts:
    part = unicodedata.normalize('NFKD', part)
    part = part.encode('ASCII', 'ignore')
    english += part.capitalize() + " "
  return english.strip()

def main():
  print p2englishPN(u"guān Xūkōng Zàng Púsà jīng")

if __name__ == "__main__": main()