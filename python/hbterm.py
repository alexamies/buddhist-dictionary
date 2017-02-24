# -*- coding: utf-8 -*-
"""
Utility loads terminology for the HB Reader from a tab separated file.

Column 1: Traditional Chinese
Column 2: English
Column 3: Source
Other columns: ignore
"""
import codecs
import string

import ntidict


TERMS_FILE_NAME = 'hbreader-terminology1.tsv'
NEWFILE = "hbterms-out.tsv"
MODFILE = "hbterms-mod.tsv"
START = 57942


def OpenTerms():
  """Reads the terms into a map
  """
  terms = {}
  with codecs.open(TERMS_FILE_NAME, 'r', "utf-8") as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
      fields = line.split('\t')
      if fields and len(fields) > 2:
        entry = {}
        key = fields[0]
        english = fields[1]
        if len(english.strip()) > 0:
          entry["english"] = english
          entry["source"] = fields[2]
          if len(fields) > 3:
            entry["concept"] = fields[3]
          if len(fields) > 4:
            entry["notes"] = fields[4]
          if key not in terms:
            terms[key] = entry
          else:
            entry["english"] = terms[key]["english"] + " / " + english
            terms[key] = entry
  print "OpenTerms completed with %d entries" % len(terms)
  return terms


def WriteTerms(terms, wdict):
  luid = START
  mods = 0
  with codecs.open(NEWFILE, 'w', "utf-8") as f:
    with codecs.open(MODFILE, 'w', "utf-8") as fmod:
      for t in terms:
        if t in wdict:
          w = wdict[t]
          wsid = string.atoi(w["id"])
          eng = terms[t]["english"]
          if w["english"].find(eng) == -1:
            eng = w["english"]
          else:
            eng = eng + " / " + w["english"]
          if "notes" in w and w["notes"] != u"\\N":
            notes = w["notes"]
          else:
            n = u""
            if "notes" in terms[t]:
              n = terms[t]["notes"]
            notes = GetNotes(n, terms[t]["source"], t, eng)
          s = u"%d\t%s\t%s\t%s\n" % (wsid, t, eng, notes)
          fmod.write(s)
        else:
          luid += 1
          eng = terms[t]["english"]
          simplified = u""
          pinyin = u""
          for c in t:
            if c not in wdict:
              # print "%s not in wdict" % c
              continue
            else:
              simplified += wdict[c]["simplified"]
              pinyin += wdict[c]["pinyin"]
          trad = t
          if simplified == trad:
            trad = "\\N"
          pos = "noun"
          concept = u"\\N\t\\N" 
          if "concept" in terms[t]:
            if "Person" in terms[t]["concept"]:
              concept = u"Person\t人"
          domain = u"佛教\tBuddhism"
          subdomain = u"\\N\t\\N"
          image = u"\\N"
          mp3 = u"\\N"
          n = u""
          if "notes" in terms[t]:
            n = terms[t]["notes"]
          notes = GetNotes(n, terms[t]["source"], t, eng)
          s = "%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%d\n" % (luid,
             simplified, trad, pinyin, eng, pos, concept, domain, subdomain, image, mp3, notes, luid)
          f.write(s)


def GetNotes(n, source, trad, eng):
  if source == u"One Hunderd Lessons on Monastery":
    source = u"(Hsing Yun 2012, <i>One Hundred Lessons on Monastery</i> 《僧事百講》, Fo Guang Shan Wenhua Shiye, Taiwan)"
  elif source == u"For All Living Beings":
    source = u"(Hsing Yun &amp; Smitheram, R 2010, <i>For All Living Beings: a Guide to Buddhist Practice</i>, Buddha's Light Publishing, Los Angeles)"
  elif source == u"Hundred Sayings":
    source = u"(Hsing Yun, <i>Hundred Sayings</i>, Fo Guang Shan Wenhua Shiye, Taiwan)"
  elif source == u"The Rabbit's Horn":
    source = u"(Hsing Yun &amp; Huineng 2010, <i>The Rabbit's Horn: A Commentary on the Platform Sutra</i>, Buddha's Light Publishing, Los Angeles)"
  elif source == u"Soothill":
    source = u"(SH '%s')" %trad
  elif source == u"DDB":
    source = u"(Muller, AC 2017, 'Digital Dictionary of Buddhism', <a href='http://www.buddhism-dict.net/ddb/'>http://www.buddhism-dict.net/ddb/</a>)"
  elif source == u"Hirakawa":
    source = u"(BCSD '%s')" % trad
  elif source == u"Cloud and Water":
    source = u"(Hsing Yun &amp; Stevens, R (tr.) 2004, <i>Cloud and Water: An Interpretation of Chan Poems</i>, Buddha's Light Publishing, Los Angeles)"
  elif source == u"Faxiang":
    source = u"(Cizhuang &amp; Smitheram, Robert (tr.) 2015,<i>Faxiang : a Buddhist Practitioner's Encyclopedia</i>, Fo Guang Shan International Translation Center, Los Angeles)"
  elif source == u"The Essence of Humanistic Buddhism":
    source = u"(Hsing Yun 2012, <i>The essence of humanistic Buddhism : BLIA general conference keynote speeches (1992-2012)</i>, BLIA world headquarters, Taipei, Taiwan)"
  elif source == u"PDB":
    source = u"(BL '%s')" % eng
  elif source == u"Understanding the Buddha's Light Philosophy":
    source = u"(Hsing Yun 2002, <i>Understanding the Buddha's Light Philosophy</i>, Buddha's Light Publishing, Hacienda Heights, California)"
  else:
    if len(source) > 0:
      source = u"(%s)" % source
    else:
      source = u"\\N"
  if len(n) == 0:
    notes = u"%s" % source
  else:
    notes = u"%s %s" % (n, source)
  return notes


def main():
  terms = OpenTerms()
  wdict = ntidict.OpenDictionary()
  WriteTerms(terms, wdict)


if __name__ == "__main__": main()