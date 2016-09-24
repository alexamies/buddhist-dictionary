# -*- coding: utf-8 -*-
"""
Utility for aggregating metadata from the Taisho Buddhist Canon. 
"""

import codecs
import re

CONTENTS_TXT = "../data/corpus/taisho/contents.txt"
CONTENTS_CSV = "../data/corpus/taisho/contents.csv"

tcontents = {}


def convert_to_csv():
  """
  Strips empty lines from the contents file
  """
  print "writing output to %s" % CONTENTS_CSV

  pattern = ur"T(\d\d)n0(\d\d\d)\s([\S]*) \( (\d{1,2}) 卷\)　【([\S]*)\s([\S]*)譯"
  expr = re.compile(pattern, re.UNICODE)
  with codecs.open(CONTENTS_TXT, 'r', "utf-8") as fin:
    with codecs.open(CONTENTS_CSV, 'w', "utf-8") as fout:
      for line in fin:
        line = line.strip()
        if line != "":
          m = expr.search(line)
          if m:
            v = m.group(1)
            tid = m.group(2)
            title = m.group(3)
            nscrolls = m.group(4)
            dynasty = m.group(5)
            translator = m.group(6)
            lineout = "%s\t%s\t%s\t%s\t%s\t%s\n" % (v, tid, title, nscrolls, 
                      dynasty, translator)
            fout.write(lineout)


def get_entry(tid):
  """
  Gets a Taisho entry for a given number
  """
  return tcontents[tid]


def load_contents():
  """
  Loads the Taisho contents into a dictionary indexed by Taisho number
  """
  with codecs.open(CONTENTS_CSV, 'r', "utf-8") as f:
    for line in f:
      row = line.split('\t')
      if row and len(row) >= 6:
        entry = {}
        entry["volume"] = int(row[0])
        entry["tid"] = row[1]
        entry["title"] = row[2]
        entry["nscrolls"] = int(row[3])
        entry["dynasty"] = row[4]
        entry["translator"] = row[5]
        tcontents[row[1]] = entry
  return tcontents

# Load the contents when the script is run
tcontents = load_contents()