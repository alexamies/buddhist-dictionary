# -*- coding: utf-8 -*-
"""
Utility loads the NTI Reader dictionary into a Python dictionary.

Simplified and traditional words are keys.
"""
import codecs


DICT_FILE_NAME = '../data/dictionary/words.txt'
wdict = {}


def OpenDictionary():
  """Reads the dictionary into memory
  """
  print("Opening the NTI Reader dictionary")
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
            else:
              entry['other_entries'] = []
              wdict[traditional] = entry
  print("OpenDictionary completed with %d entries" % len(wdict))
  return wdict

wdict = OpenDictionary()