# -*- coding: utf-8 -*-
"""
Utility for curation of dictionary entries in the accompanying Jupyter
notebook.
"""
import codecs
import re
import unicodedata


DICT_FILE_NAME = '../data/dictionary/words.txt'
wdict = {}


def ExtractFromColophon(colophon_cn):
  """
  Extract details on translator, volume, etc from Chinese colphon

  Parameters:
    colophon_cn: Chinese colphon
  Return
    (volume)
  """
  lines = colophon_cn.split("\n")
  n = len(lines)
  if n < 5:
    print "Only got %d lines" % n
    return

  # Volume number
  print "Line 1: '%s'" % lines[0]
  volumeEx = re.compile(ur"\d\d", re.UNICODE)
  m = volumeEx.search(lines[0])
  v = None
  if m:
    v = int(m.group())
  else:
    print "Volume not found"
  
  # Translator
  #print u"\u8B6F"
  translator = ""
  l4 = lines[3]
  print "Line 4: '%s' (%d)" % (l4, len(l4))
  if len(l4) < 2:
    print "Translator not found"
  else:
    volumeEx = re.compile(ur"[^\u8B6F]*", re.UNICODE) # not 譯
    m = volumeEx.search(l4)
    translator = m.group()
    if translator == u"失":
      translator = u"Unknown"

  # Number of scrolls
  l6 = lines[5]
  print "Line 6: '%s'" % l6
  nscrolls = 1
  scrollsEx = re.compile(ur"[\d]+", re.UNICODE)
  m = scrollsEx.search(l6)
  if m:
    nscrolls = int(m.group())
  else:
    print "No. scrolls not found"

  return (v, translator, nscrolls)


def ExtractWords(text):
  """Extracts words from a chunk of Chinese text.

  Algorithm is based on matching words in the dictionary maximizing the length
  of each word. Returns raw bytes to make Pandas happy

  Not finished yet.

  Args:
    text: the text to match, simplified or traditional Chinese, no punctuation

  Returns:
    A list of words
  """
  words = []
  i = 0
  length = len(text)
  #print(u'ExtractWords got text %s' % text)
  while i < length:
    j = length - 1
    #print(u'i = %d, j = %d, c: %s' % (i, j, text[i]))
    while j >= i :
      if j == i:
        #print('Adding word at j == i to list')
        words.append(text[i].encode("utf-8"))
        break
      #print(u'j = %d, c: %s' % (j, text[j]))
      possible = text[i:j+1]
      #print('Testing if possible word of length %d is in dictionary' % len(possible))
      if possible in wdict:
        #print(u'Adding dictionary word %s' % possible)
        words.append(possible.encode("utf-8"))
        break
      j -= 1
    i = j + 1
  return words


def OpenDictionary():
  """Reads the dictionary into memory
  """
  with codecs.open(DICT_FILE_NAME, 'r', "utf-8") as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
      fields = line.split('\t')
      if fields and len(fields) >= 10:
        entry = {}
        entry['id'] = fields[0]
        entry['simplified'] = fields[1]
        entry['traditional'] = fields[2]
        entry['pinyin'] = fields[3]
        entry['english'] = fields[4]
        entry['grammar'] = fields[5]
        if fields and len(fields) >= 15 and fields[14] != '\\N':
          entry['notes'] = fields[14]
        traditional = entry['traditional']
        key = entry['simplified']
        if key not in wdict:
          entry['other_entries'] = []
          wdict[key] = entry
          if traditional != '\\N':
          	wdict[traditional] = entry
        else:
          wdict[key]['other_entries'].append(entry)
          if traditional != '\\N':
          	if traditional in wdict:
          	  wdict[traditional]['other_entries'].append(entry)
  #print "OpenDictionary completed"
  return wdict


def P2englishPN(pinyin):
  """
  Converts a pinyin string to an English proper noun

  Takes a pinyin string and returns a string with the diacritics removed and
  initial letters capitalized, as a guess for the English proper noun.
  """
  english = u""
  parts = pinyin.split(" ")
  for part in parts:
    part = unicodedata.normalize('NFKD', part)
    part = part.encode('ASCII', 'ignore')
    english += part.capitalize() + " "
  return english.strip()

def WriteColophon(tid, colophon_cn, volume, english, traditional, url, 
                  nscrolls = 1, kid = 0, sanskrit = u"",
                  translator = u"Unknown", dynasty = u"", daterange = u""):
  """
  Write the colophon to a file

  Parameters:
    tid: Taisho number, an integer
    colophon_cn: the colophon in Chinese
    volume: Taisho volume number
    english: English title
    traditional: Taisho title in Chinese
    url: The URL of the text at CBETA
    nscrolls: number of scrolls, an integer
    kid: Korean canon number, an integer
    sanskrit: Sanskrit title
    translator: Translator of the text
  """

  filename = "../corpus/taisho/t0%d_00.txt" % tid
  print "Writing colophon to %s" % filename
  with codecs.open(filename, 'w', "utf-8") as f:
    kReference = u""
    if kid != 0:
      if sanskrit != "":
        kReference = u"Sanskrit title and date "
      else:
        kReference = u"Date "
      kReference += u"%s from Lancaster (Lancaster 2004, 'K %d')\n" % (daterange, 
                    kid)
    dynastyRef = u""
    if dynasty != u"":
      dynastyRef = u"Translated by %s in the %s in %d scroll(s)\n" % (translator,
                   dynasty, nscrolls)
    datestr = u"2016-09-15"

    f.write("<h4>Colophon</h4>\n")
    f.write(u"%s\n\n" % colophon_cn)
    f.write(u"Volume %d, No. %d\n" % (volume, tid))
    f.write(u"%s\n" % english)
    f.write(u"%s\n\n" % dynastyRef)
    f.write(u"<h4>Notes</h4>\n")
    if kid > 0:
      f.write(u"\n%s\n" % kReference)
    f.write(u"English translations: None\n\n")
    f.write(u"<h4>Primary Source</h4>\n")
    f.write(u"%s, 《%s》 '%s,' in <i>Taishō shinshū Daizōkyō</i> "
            u"《大正新脩大藏經》, in Takakusu Junjiro, ed., (Tokyo: Taishō "
            u"Shinshū Daizōkyō Kankōkai, 1988), Vol. %d, No. %d, Accessed "
            u"%s, <a href='%s'>%s</a>.\n\n" % (
            translator, traditional, english, volume, tid, datestr, url, url))
    f.write("<h4>References</h4>\n")
    f.write("<ol><li>Lancaster, L.R. 2004, <i>The Korean Buddhist Canon: A "
            "Descriptive Catalogue</i>, "
            "<a href='http://www.acmuller.net/descriptive_catalogue/'"
            ">http://www.acmuller.net/descriptive_catalogue</a>.</li></ol>\n")


wdict = OpenDictionary()