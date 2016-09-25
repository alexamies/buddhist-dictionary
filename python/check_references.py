# -*- coding: utf-8 -*-
"""
Utility checks references in the NTI Reader dictionary

Checking for references in the Notes field, against the CC-CEDCT dictionary,
and re-writing to a copy.
"""
import codecs


DICT_FILE_NAME = '../data/dictionary/words.txt'


def ScanDictionary():
  """Reads the dictionary into memory
  """
  with codecs.open(DICT_FILE_NAME, 'r', "utf-8") as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
  print "ScanDictionary completed"


def parseEntry(line):
  fields = line.split('\t')
  if fields and len(fields) == 16:
    entry = {}
    entry['id'] = fields[0]
    entry['simplified'] = fields[1]
    entry['traditional'] = fields[2]
    entry['pinyin'] = fields[3]
    entry['english'] = fields[4]
    entry['grammar'] = fields[5]
    entry['concept_cn'] = fields[6]
    entry['concept_en'] = fields[7]
    entry['topic_cn'] = fields[8]
    entry['topic_en'] = fields[9]
    entry['parent_cn'] = fields[10]
    entry['parent_en'] = fields[11]
    entry['image'] = fields[12]
    entry['mp3'] = fields[13]
    entry['notes'] = fields[14]
    entry['headword'] = fields[15]
  else:
    print "Only found %d filds in line '%s'" % (len(fields), line)
  return entry
