# -*- coding: utf-8 -*-
"""
Utility for curation of dictionary entries in the accompanying Jupyter
notebook.
"""
import codecs
import re
import unicodedata
from datetime import date

from korean import getkoreanid
import ntidict
import taisho_contents


DICT_FILE_NAME = '../data/dictionary/words.txt'
wdict = {}


def ExtractFromColophon(colophon_cn):
  """
  Extract details on translator, volume, etc from Chinese colphon

  Parameters:
    colophon_cn: Chinese colphon
  """
  v = None
  tid = u""
  dynasty = u""
  translator = u"Unknown"
  nscrolls = 1

  lines = colophon_cn.split("\n")
  n = len(lines)
  if n < 5:
    print "Only got %d lines" % n

  for line in lines:
    #print "Line: '%s'" % line

    # Volume number
    isVolumeEx = re.compile(ur"^第[\s|\S]*", re.UNICODE)
    if isVolumeEx.match(line):
      #print "Got volume match"
      volumeEx = re.compile(ur"第 (\d\d)", re.UNICODE)
      m = volumeEx.search(line)
      if m:
        v = int(m.group(1))
      else:
        print "Volume not found"
      tidEx = re.compile(ur"No. 0(\d\d\d[\S]{0,1})", re.UNICODE)
      m = tidEx.search(line)
      if m:
        tid = m.group(1)
      else:
        print "Taisho number not found"
  
    # Translator
    isTranslatorEx = re.compile(ur"[\s|\S]*譯", re.UNICODE)
    if isTranslatorEx.match(line):
      #print "Got translator match"
      chunks = line.split()
      if len(chunks) == 2:
        if chunks[0] in wdict:
          dynasty = GetDynastyEn(chunks[0])
      line = chunks[1]
      if len(line) < 2:
        print "Translator not found"
      else:
        volumeEx = re.compile(ur"[^\u8B6F]*", re.UNICODE) # not 譯
        m = volumeEx.search(line)
        translator = m.group()
        if translator == u"失" or translator == u"闕":
          translator = u"Unknown"
        elif translator in wdict:
          translator = wdict[translator]["english"]
          transTokens = translator.split("/")
          translator = transTokens[0].strip()
        else:
          if translator[-1] == u"等":
            translator = translator[:-1]
            if translator in wdict:
              translator = wdict[translator]["english"]
              transTokens = translator.split("/")
              translator = transTokens[0].strip()
              translator += " and others"
          else:
            print u"Translator %s not found" % translator

    # Number of scrolls
    isScrollsEx = re.compile(ur"共[\s|\S]*", re.UNICODE)
    if isScrollsEx.match(line):
      #print "Got scrolls match"
      scrollsEx = re.compile(ur"[\d]+", re.UNICODE)
      m = scrollsEx.search(line)
      if m:
        nscrolls = int(m.group())
      else:
        print "No. scrolls not found"
  return (v, tid, nscrolls, translator, dynasty)


def GetDynastyEn(dynasty_cn):
  """
  Gets the dynasty in English and does some mangling to make it readable."""
  dynasty_en = dynasty_cn
  if dynasty_cn == u"梁":
    dynasty_en = u"Liang" # Not a bridge
  elif dynasty_cn == u"明":
    dynasty_en = u"Ming" # Not bright
  elif dynasty_cn == u"清":
    dynasty_en = u"Qing" # Not clear
  else:
    if dynasty_cn in wdict:
      dynasty_en = wdict[dynasty_cn]["english"]
      dynasty_en = dynasty_en.replace("Dynasty", "")
      dynasty_en = dynasty_en.strip()
      dynastyTokens = dynasty_en.split("/")
      dynasty_en = dynastyTokens[0].strip()
  return dynasty_en

def GetCompiledByEn(compiledby_cn):
  """
  Gets the dynasty in English and does some mangling to make it readable."""
  compiledby_en = compiledby_cn
  if compiledby_cn in wdict:
    compiledby_en = wdict[compiledby_cn]["english"]
    tokens = compiledby_en.split("/")
    compiledby_en = tokens[0].strip()
  return compiledby_en

def GetHowEn(how_cn):
  """
  Gets the dynasty in English and does some mangling to make it readable."""
  how_en = how_cn
  how_dict = {u"譯": "Translated",
              u"集": "Compiled",
              u"述": "Narrated",
              u"撰": "Composed",
              u"說": "Spoken",
              u"記": "Recorded",
              u"請來": "Invited",
              u"注": "Recorded",
              u"校": "Taught"
              }
  if how_cn in how_dict:
    how_en = how_dict[how_cn]
  return how_en


def GetEntry(tid):
  """
  Gets a Taisho entry for a given number

  Translates the parts into English
  """
  entry = taisho_contents.get_entry(tid)
  entry["dynasty_en"] = GetDynastyEn(entry["dynasty"])
  entry["translator_en"] = GetTranslatorEn(entry["translator"])
  entry["compiledby_en"] = GetCompiledByEn(entry["compiledby_cn"])
  entry["how_en"] = GetHowEn(entry["how_cn"])
  return entry


def GetTranslatorEn(translator):
  """
  Gets the translator nama in English doing mangling to make it readable."""
  translator_en = translator
  if translator == u"失" or translator == u"闕":
    translator_en = u"Unknown"
  elif translator in wdict:
    translator_en = wdict[translator]["english"]
    transTokens = translator_en.split("/")
    translator_en = transTokens[0].strip()
  else:
    print "Translator %s not in dictionary" % translator
    if translator and translator[-1] == u"等":
      translator = translator[:-1]
    if translator in wdict:
      translator_en = wdict[translator]["english"]
      transTokens = translator_en.split("/")
      translator_en = transTokens[0].strip()
      translator_en += " and others"
    else:
      print u"GetTranslatorEn: Translator '%s' not found" % translator
  return translator_en


def InsertIntoVolume(volume, text):
  """
  Inserts the given text into the HTML file for the the Taisho volume.

  A marker will be used to find the right place to insert the text.
  """
  file = "../html/taisho/t%d.html" % volume
  doc = u""
  tagEx = re.compile(r"[\s]*\{\{next_title\}\}")
  with codecs.open(file, 'r', "utf-8") as f:
    for line in f:
      if tagEx.match(line):
        doc += tagEx.sub(text, line)
      else:
        doc += line

  with codecs.open(file, 'w', "utf-8") as outfile:
    outfile.write(doc)


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


def WriteCollectionEntry(tid, title, translator, daterange, genre, how_en):
  """
  Appends an entry to the collection file
  """
  tidStr = tid
  if tid < 1000:
    tidStr = "0%s" % tid
  translatedBy = ""
  if how_en != "" and translator != "":
    translatedBy = u"%s by %s" % (how_en, translator)
  entry = u"\ntaisho/t%s.csv\ttaisho/t%s.html\t%s\t%s\ttaisho/t%s_00.txt\tTaishō\tSūtra\t%s\t%s" % (
    tidStr, tidStr, title, translatedBy, tidStr, daterange, genre)
  filename = "../data/corpus/collections.csv"
  with codecs.open(filename, 'a', "utf-8") as f:
    f.write(entry)


def WriteColophon(tid, colophon_cn, volume, english, traditional, url, 
                  nscrolls = 1, kid = 0, sanskrit = "",
                  translator = "Unknown", dynasty = "", daterange = "",
                  compiledBy = "", how_en = "translated"):
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

  tidStr = tid
  if tid < 1000:
    tidStr = "0%s" % tid
  filename = "../corpus/taisho/t%s_00.txt" % tidStr
  print "Writing colophon to %s" % filename
  with codecs.open(filename, 'w', "utf-8") as f:
    kReference = u""
    if kid != "0":
      if sanskrit != "":
        kReference = u"Sanskrit title and date "
      else:
        kReference = u"Date "
      kReference += u"%s from Lancaster (Lancaster 2004, 'K %s')" % (daterange, 
                    kid)
    scrollStr = u"scroll"
    if nscrolls > 1:
      scrollStr = u"scrolls"
    dynastyRef = u""
    if compiledBy != "":
      compiledbyRef = "Compiled by %s. " % compiledBy
    if dynasty != u"":
      dynastyRef = u"%s by %s in the %s in %d %s" % (how_en, translator,
                   dynasty, nscrolls, scrollStr)
    elif translator != u"":
      dynastyRef = u"%s by %s in %d %s" % (how_en, translator,
                   nscrolls, scrollStr)
    datestr = date.today().strftime("%Y-%m-%d")

    f.write("<h4>Colophon</h4>\n")
    f.write(u"%s\n\n" % colophon_cn)
    f.write(u"Volume %d, No. %s\n" % (volume, tid))
    f.write(u"%s\n" % english)
    f.write(u"%s\n\n" % dynastyRef)
    f.write(u"<h4>Notes</h4>\n")
    if kid > 0:
      f.write(u"\n%s\n" % kReference)
    f.write(u"English translations: None\n\n")
    f.write(u"<h4>Primary Source</h4>\n")
    if translator.strip() == "":
      translator == "Unknown"
    f.write(u"%s, 《%s》 '%s,' in <i>Taishō shinshū Daizōkyō</i> "
            u"《大正新脩大藏經》, in Takakusu Junjiro, ed., (Tokyo: Taishō "
            u"Shinshū Daizōkyō Kankōkai, 1988), Vol. %d, No. %s, Accessed "
            u"%s, <a href='%s'>%s</a>.\n\n" % (
            translator, traditional, english, volume, tid, datestr, url, url))
    if kid != "0":
      f.write("<h4>References</h4>\n")
      f.write("<ol><li>Lancaster, L.R. 2004, <i>The Korean Buddhist Canon: A "
              "Descriptive Catalogue</i>, "
              "<a href='http://www.acmuller.net/descriptive_catalogue/'"
              ">http://www.acmuller.net/descriptive_catalogue</a>.</li></ol>\n")



def WriteWordEntry(wordLine):
  """
  Appends an entry to the words file
  """
  filename = "../data/dictionary/words.txt"
  with codecs.open(filename, 'a', "utf-8") as f:
    f.write("\n" + wordLine)
  print "Wrote line to words file"


wdict = ntidict.OpenDictionary()