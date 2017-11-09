# -*- coding: utf-8 -*-
"""
Utility loads the CC-CEDICT dictionary into a Python dictionary.

Assumes that the cedict_ts.u8 file is in the directory DICT_FILE_NAME below.
Traditional Chinese words are keys.
"""
import codecs
import re


DICT_FILE_NAME = 'cedict_1_0_ts_utf-8_mdbg.txt'

cedict = {}
pattern = re.compile(ur"(.*) (.*) \[(.*)\] /(.*)/", re.UNICODE)


def OpenDictionary():
  """Reads the dictionary into memory
  """
  with codecs.open(DICT_FILE_NAME, 'r', "utf-8") as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
      if line[0] == "#":
        continue
      m = pattern.search(line)
      if m:
        entry = {}
        key = m.group(1)
        entry['traditional'] = key
        entry['simplified'] = m.group(2)
        entry['pinyin'] = m.group(3)
        entry['english'] = m.group(4)
        if key not in cedict:
          entry['other_entries'] = []
          cedict[key] = entry
        else:
          cedict[key]['other_entries'].append(entry)
      else:
        print u"Could not parse line '%s'" % line
  print "cccedict.OpenDictionary completed with %d entries" % len(cedict)
  return cedict

cedict = OpenDictionary()