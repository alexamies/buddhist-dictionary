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

  pattern = ur"【(.*)】"
  pattern1 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【([\S]*)\s([\S]*)([譯|集|述|撰|說|記|請來|注|校|造|錄|治定|註|解|略|補|修|作|著|緝|纂|編|唱|輯|箋])】"
  pattern2 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【([\S]*)([譯|集|述|撰|說|記|請來|注|校|造|錄|治定|註|解|略|補|修|作|著|纂|編|唱|輯|箋])】"
  pattern3 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【([\S]+)([集|撰|造|頌|釋|作|說|論|本|糅|製|述|要|解])\s([\S]+)\s([\S]+)([譯|集|述|撰|說|記|請來|注|校|造|錄|治定|註|解|略|補|修|作|著|纂|編|唱|輯|箋])】"
  pattern4 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【([\S]+)([集|撰|造|頌|釋|作|說|論|本|糅|製|述|要|解])\s([\S]+)[釋|論|說]\s([\S]+)\s([\S]+)([譯|集|述|撰|說|記|請來|注|校|造|錄|治定|註|解|略|補|修|作|著|纂|編|唱|輯|箋])】"
  pattern5 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【】"
  pattern6 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【(偈本)([\S]+)\s釋論([\S]+)\s([\S]+)\s([\S]+)([譯|集|述|撰|說|記|請來|注|校|造|錄|解|略|註|補|修|作|著|纂|編|唱|輯|箋])】"
  pattern7 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【([\S]+)\s([\S]+)([集|撰|造|頌|釋|作|說|論|本|糅|製|述|要|解|古])[\s|、|．]([\S]+)[\s|、]([\S]+)([治定|略|註|補|修|作|著|撰|述|纂|編|唱|輯|箋])】"
  pattern8 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【([\S]+)\s([\S]+)([集|撰|造|頌|釋|作|說|論|本|糅|製|述|要|解])\s([\S]+)([譯|集|述|撰|說|記|請來|注|校|造|錄|解|略|註|補|修|作|著|纂|編|唱|輯|箋])】"
  pattern9 = ur"T(\d\d)n[0]{0,3}([1-9]{1,3}[\S]*)\s([\S]*) \( (\d{1,3}) 卷\)　【([\S]*)\s([\S]*)([答])】"
  expr = re.compile(pattern, re.UNICODE)
  expr1 = re.compile(pattern1, re.UNICODE)
  expr2 = re.compile(pattern2, re.UNICODE)
  expr3 = re.compile(pattern3, re.UNICODE)
  expr4 = re.compile(pattern4, re.UNICODE)
  expr5 = re.compile(pattern5, re.UNICODE)
  expr6 = re.compile(pattern6, re.UNICODE) # 1566
  expr7 = re.compile(pattern7, re.UNICODE) # 1701
  expr8 = re.compile(pattern8, re.UNICODE) # 1705
  expr9 = re.compile(pattern9, re.UNICODE) # 1856
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
        explainedBy = ""
        lineout = ""
        attribution_cn = ""
        if line != "":
          m = expr.search(line)
          if m:
            attribution_cn = m.group(1)
            #print u"attribution_cn: %s in line %s\n" % (attribution_cn, line)
          else:
            print u"cannot find attribution_cn in line %s\n" % line
          m1 = expr1.search(line)
          m2 = expr2.search(line)
          m3 = expr3.search(line)
          m4 = expr4.search(line)
          m5 = expr5.search(line)
          m6 = expr6.search(line)
          m7 = expr7.search(line)
          m8 = expr8.search(line)
          m9 = expr9.search(line)
          if m1:
            #print u"%s: m1" % line
            v = m1.group(1)
            tid = m1.group(2)
            title = m1.group(3)
            nscrolls = m1.group(4)
            dynasty = m1.group(5)
            translator = m1.group(6)
            how = m1.group(7)
          elif m2:
            #print u"%s: m2" % line
            v = m2.group(1)
            tid = m2.group(2)
            title = m2.group(3)
            nscrolls = m2.group(4)
            translator = m2.group(5)
            how = m2.group(6)
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
          elif m4:
            # Explained by 
            #print u"%s: m4" % line
            v = m4.group(1)
            tid = m4.group(2)
            title = m4.group(3)
            nscrolls = m4.group(4)
            compiledBy = m4.group(5)
            compiledHow = m4.group(6)
            explainedBy = m4.group(7)
            dynasty = m4.group(8)
            translator = m4.group(9)
            how = m4.group(10)
          elif m5:
            #print u"%s: m5" % line
            v = m5.group(1)
            tid = m5.group(2)
            title = m5.group(3)
            nscrolls = m5.group(4)
          elif m6:
            # Explained by 
            #print u"%s: m6" % line
            v = m6.group(1)
            tid = m6.group(2)
            title = m6.group(3)
            nscrolls = m6.group(4)
            compiledHow = m6.group(5)
            compiledBy = m6.group(6)
            explainedBy = m6.group(7)
            dynasty = m6.group(8)
            translator = m6.group(9)
            how = m6.group(10)
          elif m7:
            # Explained by 
            #print u"%s: m7" % line
            v = m7.group(1)
            tid = m7.group(2)
            title = m7.group(3)
            nscrolls = m7.group(4)
            compiledBy = m7.group(6)
            compiledHow = m7.group(7)
            dynasty = m7.group(8)
            translator = m7.group(9)
            how = m7.group(10)
          elif m8:
            # Explained by 
            print u"%s: m8" % line
            v = m8.group(1)
            tid = m8.group(2)
            title = m8.group(3)
            nscrolls = m8.group(4)
            dynasty = m8.group(5)
            compiledBy = m8.group(6)
            compiledHow = m8.group(7)
            translator = m8.group(8)
            how = m8.group(9)
          if m9:
            #print u"%s: m9" % line
            v = m9.group(1)
            tid = m9.group(2)
            title = m9.group(3)
            nscrolls = m9.group(4)
            dynasty = m9.group(5)
            translator = m9.group(6)
            how = m9.group(7)
          lineout = "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (v, tid, title, nscrolls, 
                      dynasty, translator, compiledBy, how, compiledHow, explainedBy,
                      attribution_cn)
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
      if row and len(row) == 11:
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
        entry["explainedby_cn"] = row[9].strip()
        entry["attribution_cn"] = row[10].strip()
        tcontents[row[1]] = entry
      else:
        print "Problem with: '%s'" % line
  return tcontents


# Load the contents when the script is run
tcontents = load_contents()