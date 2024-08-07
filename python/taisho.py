# -*- coding: utf-8 -*-
"""
Utility for aggregating metadata from the Taisho Buddhist Canon. 
"""

import codecs
import xml.etree.ElementTree as ET
import re
import sys
import urllib2

from bs4 import BeautifulSoup

import html2text

sys.setrecursionlimit(2000)

isEndEx = re.compile(ur"(.*)網路分享", re.UNICODE)
isNulEx = re.compile(ur"\0", re.UNICODE)
isNavEx = re.compile(ur"▲", re.UNICODE)


def geturl(volume, tid):
  """
  Get the URL of the entry in the Taisho matching the given Taisho id.

  Also, check that the URL is correct by doing a GET.
  """
  url = "http://tripitaka.cbeta.org/T%dn0%s" % (volume, tid)
  if tid > 999:
    url = "http://tripitaka.cbeta.org/T%dn%s" % (volume, tid)
  print "taisho.py, url = %s" % url
  response = urllib2.urlopen(url)  
  return url


def saveScrolls(volume, tid, numscrolls, title):
  """
  Saves the series of scrolls from the title.

  Saves the files to the Taisho corpus folder on local disk
  """
  for i in range(1, numscrolls + 1):
  	saveScrollFromWeb(volume, tid, i, title)
  #saveScrollfromXML(volume, tid, 1)


def saveScrollfromXML(volume, tid, scrollno):
  """
  Get the scroll from XML and save plain text to local disk.
  """
  cbeta_home = "/Users/alex/Documents/code/cbeta/xml-p5/T"
  filename = "%s/T%d/T%dn%s.xml" % (cbeta_home, volume, volume, tid)
  tree = ET.parse(filename)
  root = tree.getroot()
  text = ET.tostring(root, encoding="utf-8", method="text").decode('utf8')
  doc = ""
  header = True
  for line in text.split('\n'):
    if line.strip() != "":
      if header or line[0] != "\t":
        doc += line + "\n"
      if line.find(u"蕭鎮國大德提供") != -1:
        header = False

  doc += u"""\n\n本網站係採用 Creative Commons 姓名標示-非商業性-相同方式分享 3.0 
  台灣 (中華民國) 授權條款授權.Copyright ©1998-2016 CBETA\n"""

  tidStr = tid
  if tid < 1000:
    tidStr = "0%s" % tid
  scrollStr = "0%d" % scrollno
  if 10 <= scrollno and scrollno < 100:
    scrollStr = "%d" % scrollno
  elif 100 <= scrollno:
    scrollStr = "%d" % scrollno
  file = "../corpus/taisho/t%s_%s.txt" % (tidStr, scrollStr)
  with codecs.open(file, 'w', "utf-8") as outfile:
    outfile.write(doc)


def saveScrollFromWeb(volume, tid, scrollno, title):
  """
  Fetch the scroll over HTTP and save plain text to local disk.
  """
  print "saveScrollFromWeb, title: %s" % title
  scrollStr = "00%d" % scrollno
  if 10 <= scrollno and scrollno < 100:
    scrollStr = "0%d" % scrollno
  elif 100 <= scrollno and scrollno < 1000:
  	scrollStr = "%d" % scrollno
  tidStr = tid
  if tid < 1000:
    tidStr = "0%s" % tid
  url = "http://tripitaka.cbeta.org/T%dn%s_%s" % (volume, tidStr, scrollStr)
  print url
  (juanname, text) = readWebToPlainText(url, tidStr)

  if juanname == u"":
    juanname = title
  lines = text.split("\n")
  pattern = ur"(%s)(.*)" % juanname
  isTitleEx = re.compile(pattern, re.UNICODE)
  start = False
  doc = u""
  for line in lines:
    #print "line: %s" % line
    line_str = line.replace(" ", "")
    #print "line_str: %s" % line_str
    if start:
      m1 = isEndEx.search(line_str)
      m2 = isNulEx.search(line_str)
      m3 = isNavEx.search(line_str)
      if m1:
        #print "m1, line: %s" % line
        doc += line
        break
      elif m2:
        #print "m2, line: %s" % line
        line.replace("\0", "")
      elif m3:
        #print "m3, line: %s" % line
        continue
      #print "line: %s" % line
      doc += line + "\n"
    else:
      m = isTitleEx.search(line_str)
      if m:
        start = True
        print "start, juanname: %s, m.group(2): %s" % (juanname, m.group(2))
        doc = line

  doc += u"""\n\n本網站係採用 Creative Commons 姓名標示-非商業性-相同方式分享 3.0 台灣 (中華民國) 授權條款授權.
Copyright ©1998-2016 CBETA\n"""

  scrollStr = "0%d" % scrollno
  if 10 <= scrollno and scrollno < 100:
    scrollStr = "%d" % scrollno
  elif 100 <= scrollno:
  	scrollStr = "%d" % scrollno
  file = "../corpus/taisho/t%s_%s.txt" % (tidStr, scrollStr)
  with codecs.open(file, 'w', "utf-8") as outfile:
    outfile.write(doc)


def readWebToPlainText(url, tidStr):
  """
  Fetch the HTML document over HTTP and return plain text
  """
  html_doc = urllib2.urlopen(url).read().decode('utf8')
  soup = BeautifulSoup(html_doc)
  # Scroll name
  juanname = u""
  tags = soup.find_all("span", class_="juanname")
  if tags:
    juanname = tags[0].get_text().replace(" ", "")
  juanname = juanname.split("(")[0]
  # byline sometimes gets confused with scroll name
  byline = u""
  tags = soup.find_all("span", class_="byline")
  if tags:
    byline = tags[0].get_text()
  if len(byline) > 0:
    i = juanname.find(byline)
    if i > -1:
      juanname = juanname[:i]
  print "juanname' '%s', tidStr = '%s'" % (juanname, tidStr)
  main = soup.find(id=tidStr)
  text = html2text.html2text(main.prettify())
  return (juanname, text)
