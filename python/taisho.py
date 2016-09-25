# -*- coding: utf-8 -*-
"""
Utility for aggregating metadata from the Taisho Buddhist Canon. 
"""

import codecs
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
  response = urllib2.urlopen(url)  
  return url


def saveScrolls(volume, tid, numscrolls, title):
  """
  Saves the series of scrolls from the title.

  Saves the files to the Taisho corpus folder on local disk
  """
  for i in range(1, numscrolls + 1):
  	saveScrollFromWeb(volume, tid, i, title)


def saveScrollFromWeb(volume, tid, scrollno, title):
  """
  Fetch the scroll over HTTP and save plain text to local disk.
  """
  print "saveScrollFromWeb, title: %s" % title
  scrollStr = "00%d" % scrollno
  if 10 <= scrollno and scrollno < 100:
    scrollStr = "0%d" % scrollno
  elif 100 <= scrollno:
  	scrollStr = "%d" % scrollno
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
    if start:
      m1 = isEndEx.search(line)
      m2 = isNulEx.search(line)
      m3 = isNavEx.search(line)
      if m1:
        print "m1, line: %s" % line
        doc += m.group(2) + "\n"
        break
      elif m2:
        print "m2, line: %s" % line
        line.replace("\0", "")
      elif m3:
        print "m3, line: %s" % line
        continue
      #print "line: %s" % line
      doc += line + "\n"
    else:
      m = isTitleEx.search(line)
      if m:
        start = True
        print "start, juanname: %s, m.group(2): %s" % (juanname, m.group(2))
        doc = juanname + "\n" + m.group(2) + "\n"

  doc += u"""\n\n本網站係採用 Creative Commons 姓名標示-非商業性-相同方式分享 3.0 台灣 (中華民國) 授權條款授權.
Copyright ©1998-2016 CBETA\n"""

  scrollStr = "0%d" % scrollno
  if 10 <= scrollno and scrollno < 100:
    scrollStr = "%d" % scrollno
  elif 100 <= scrollno:
  	scrollStr = "%d" % scrollno
  file = "../corpus/taisho/t0%s_%s.txt" % (tid, scrollStr)
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
  print "juanname' '%s'" % juanname
  main = soup.find(id=tidStr)
  text = html2text.html2text(main.prettify())
  return (juanname, text)
