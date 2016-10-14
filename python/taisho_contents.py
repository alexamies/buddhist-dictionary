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

  pattern = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【([\S]*)\s([\S]*)([譯|集|述|撰|說|記|請來|注|校|造|錄])】"
  pattern2 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【([\S]*)([譯|集|述|撰|說|記|請來|注|校|造|錄])】"
  pattern3 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【([\S]+)([集|撰|造])\s([\S]+)\s([\S]+)([譯|集|述|撰|說|記|請來|注|校|造|錄])】"
  pattern5 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【】"
  expr = re.compile(pattern, re.UNICODE)
  expr2 = re.compile(pattern2, re.UNICODE)
  expr3 = re.compile(pattern3, re.UNICODE)
  expr5 = re.compile(pattern5, re.UNICODE)
  with codecs.open(CONTENTS_TXT, 'r', "utf-8") as fin:
    with codecs.open(CONTENTS_CSV, 'w', "utf-8") as fout:
      for line in fin:
        line = line.strip()
        tid = ""
        dynasty = ""
        translator = ""
        compiledBy = ""
        how = ""
        compiledHow = ""
        lineout = ""
        if line != "":
          m = expr.search(line)
          m2 = expr2.search(line)
          m3 = expr3.search(line)
          m5 = expr5.search(line)
          if m:
            #print u"%s: m1" % line
            v = m.group(1)
            tid = m.group(2)
            title = m.group(3)
            nscrolls = m.group(4)
            dynasty = m.group(5)
            translator = m.group(6)
            how = m.group(7)
            lineout = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (v, tid, title, nscrolls, 
                      dynasty, translator, compiledBy, how, compiledHow)
            fout.write(lineout)
          elif m2:
            #print u"%s: m2" % line
            v = m2.group(1)
            tid = m2.group(2)
            title = m2.group(3)
            nscrolls = m2.group(4)
            translator = m2.group(5)
            how = m2.group(6)
            lineout = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (v, tid, title, nscrolls, 
                      dynasty, translator, compiledBy, how, compiledHow)
            fout.write(lineout)
          elif m3:
            #print u"%s: m3" % line
            v = m3.group(1)
            tid = m3.group(2)
            title = m3.group(3)
            nscrolls = m3.group(4)
            compiledBy = m3.group(5)
            compiledHow = m3.group(6)
            dynasty = m3.group(7)
            translator = m3.group(8)
            how = m3.group(9)
            lineout = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (v, tid, title, nscrolls, 
                      dynasty, translator, compiledBy, how, compiledHow)
            fout.write(lineout)
          elif m5:
            #print u"%s: m5" % line
            v = m5.group(1)
            tid = m5.group(2)
            title = m5.group(3)
            nscrolls = m5.group(4)
            lineout = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (v, tid, title, nscrolls, 
                      dynasty, translator, compiledBy, how, compiledHow)
            fout.write(lineout)


def get_entry(tid):
  """
  Gets a Taisho entry for a given number

  The parts are all in Chinese
  """
  return tcontents[tid]


def load_contents():
  """
  Loads the Taisho contents into a dictionary indexed by Taisho number
  """
  with codecs.open(CONTENTS_CSV, 'r', "utf-8") as f:
    for line in f:
      row = line.split('\t')
      if row and len(row) == 9:
        entry = {}
        entry["volume"] = int(row[0])
        entry["tid"] = row[1]
        entry["title"] = row[2]
        entry["nscrolls"] = int(row[3])
        entry["dynasty"] = row[4]
        entry["translator"] = row[5].strip()
        entry["compiledby_cn"] = row[6].strip()
        entry["how_cn"] = row[7].strip()
        entry["compiled_how_cn"] = row[8].strip()
        tcontents[row[1]] = entry
      else:
        print "Problem with: '%s'" % line
  return tcontents


# Load the contents when the script is run
tcontents = load_contents()