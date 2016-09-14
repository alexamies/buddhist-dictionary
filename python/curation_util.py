# -*- coding: utf-8 -*-
"""
Utility for curation of dictionary entries in the accompanying Jupyter
notebook.
"""
import codecs
import unicodedata


DICT_FILE_NAME = '../data/dictionary/words.txt'
wdict = {}


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


def TextExtractWords(text):
  words = ExtractWords(text)
  print "result"
  for w in words:
    print u"  Word: %s" % w.decode("utf-8")


def main():
  #print P2englishPN(u"guān Xūkōng Zàng Púsà jīng")
  #TextExtractWords(u"你好世界")
  #TextExtractWords(u"你好美國")
  TextExtractWords(u"经")

wdict = OpenDictionary()
if __name__ == "__main__": main()