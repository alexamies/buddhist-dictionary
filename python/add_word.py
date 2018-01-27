# -*- coding: utf-8 -*-
"""
Utility loads terminology for the dictionary from a comma separated file.

Column 1: Traditional Chinese
Column 2: English
Column 3: Source
Other columns: ignore
"""
import codecs
import string

import ntidict
from char_util import ToSimplified
from ntidict import OpenDictionary


TERMS_FILE_NAME = 'add_words20171211.tsv'
NEWFILE = "add_words20171211-out.tsv"
START = 82595


def OpenTerms():
  """Reads the terms into a map
  """
  terms = []
  ntidict = OpenDictionary()
  with codecs.open(TERMS_FILE_NAME, 'r', "utf-8") as f:
    for line in f:
      line = line.strip()
      if not line or line.startswith("#"):
        continue
      fields = line.split('\t')
      if len(fields) < 13:
        print "len(fields) < 13 %d, %s" %  (len(fields), line)
        continue
      entry = {}
      simplified = fields[0]
      key = fields[1]
      if key in ntidict:
        print u"%s is already in nti dict" %  key
        continue
      english = fields[2]
      if len(english.strip()) == 0:
        print "len(english.strip()) == 0, %s" %  line
        continue
      grammar = fields[3]
      concept_cn = fields[4]
      concept_en = fields[5]
      domain_cn = fields[6]
      domain_en = fields[7]
      subdomain_cn = fields[8]
      subdomain_en = fields[9]
      notes = fields[12]
      entry["simplified"] = simplified
      if key == simplified:
        entry["traditional"] = u"\\N"
      else:
        entry["traditional"] = key
      _, _, pinyin = ToSimplified(key)
      entry["pinyin"] = pinyin
      entry["english"] = english
      entry["grammar"] = grammar
      entry["concept_cn"] = concept_cn
      entry["concept_en"] = concept_en
      entry["domain_cn"] = domain_cn
      entry["domain_en"] = domain_en
      entry["subdomain_cn"] = subdomain_cn
      entry["subdomain_en"] = subdomain_en
      entry["notes"] = notes
      terms.append(entry)
  print "OpenTerms completed with %d entries" % len(terms)
  return terms


def WriteTerms(terms, wdict):
  luid = START
  with codecs.open(NEWFILE, 'w', "utf-8") as f:
    for t in terms:
      simplified = t["simplified"]
      if simplified not in wdict:
        luid += 1
        traditional = t["traditional"]
        pinyin = t["pinyin"]
        eng = t["english"]
        grammar = t["grammar"]
        concept_cn = t["concept_cn"]
        concept_en = t["concept_en"]
        domain_cn = t["domain_cn"]
        domain_en = t["domain_en"]
        subdomain_cn = t["subdomain_cn"]
        subdomain_en = t["subdomain_en"]
        image = u"\\N"
        mp3 = u"\\N"
        notes = t["notes"]
        s = "%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%d\n" % (luid,
           simplified, traditional, pinyin, eng, grammar, concept_cn, concept_en,
           domain_cn, domain_en, subdomain_cn, subdomain_en, image, mp3, notes, luid)
        f.write(s)


def main():
  terms = OpenTerms()
  wdict = ntidict.OpenDictionary()
  WriteTerms(terms, wdict)


if __name__ == "__main__": main()