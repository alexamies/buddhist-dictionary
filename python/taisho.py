# -*- coding: utf-8 -*-
"""
Utility for aggregating metadata from the Taisho Buddhist Canon. 
"""

import codecs
import re
import urllib2

from bs4 import BeautifulSoup


def geturl(volume, tid):
  """
  Get the URL of the entry in the Taisho matching the given Taisho id.

  Also, check that the URL is correct by doing a GET.
  """
  url = "http://tripitaka.cbeta.org/T%dn0%s" % (volume, tid)
  response = urllib2.urlopen(url)  
  return url


def htmlToPlainText(html, tidStr):
  soup = BeautifulSoup(html)
  juanname = u""
  tags = soup.find_all("span", class_="juanname")
  if tags:
    juanname = tags[0].get_text()
  print "juanname: %s" % juanname
  text = soup.find(id=tidStr).get_text()
  lines = text.split("\n")
  pattern = ur"(%s)(.*)" % juanname
  isTitleEx = re.compile(pattern, re.UNICODE)
  isEndEx = re.compile(ur"網路分享", re.UNICODE)
  start = False
  doc = u""
  for line in lines:
    if start:
      doc += line.replace(u"[", u"\n[").replace(u"【", u"\n【")
      m = isEndEx.search(line)
      if m:
        break
    else:
      m = isTitleEx.search(line)
      if m:
        start = True
        doc = m.group(1) + "\n" + m.group(2).replace(u"[", u"\n[").replace(u"【", u"\n【")

  doc += u"""\n\n本網站係採用 Creative Commons 姓名標示-非商業性-相同方式分享 3.0 台灣 (中華民國) 授權條款授權.
Copyright ©1998-2016 CBETA\n"""
  return text


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
  pattern = ur"%s(.*)" % juanname
  isTitleEx = re.compile(pattern, re.UNICODE)
  isEndEx = re.compile(ur"網路分享", re.UNICODE)
  start = False
  doc = u""
  for line in lines:
    if start:
      doc += line.replace(u"[", u"\n[").replace(u"【", u"\n【")
      m = isEndEx.search(line)
      if m:
        break
    else:
      m = isTitleEx.search(line)
      if m:
        start = True
        doc = juanname + "\n" + m.group(1).replace(u"[", u"\n[").replace(u"【", u"\n【")

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
  html_doc = urllib2.urlopen(url).read()
  soup = BeautifulSoup(html_doc)
  juanname = u""
  tags = soup.find_all("span", class_="juanname")
  if tags:
    juanname = tags[0].get_text()
  text = soup.find(id=tidStr).get_text()
  return (juanname, text)
  """
  [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
  text = ''
  #for text_str in soup.strings:
  for tag in soup.find_all():
    text_str = tag.string
    #print(text_str)
    if text_str and tag.name == u'p':
      text_str = text_str.strip() + '\n'
    elif text_str and tag.name == u'div':
      text_str = text_str.strip() + '\n'
    elif tag.name == u'h1':
      continue
    elif text_str and tag.name == u'h2':
      text_str = text_str.strip() + '\n'
    elif text_str and tag.name == u'h3':
      text_str = text_str.strip() + '\n'
    elif text_str and tag.name == u'h4':
      text_str = text_str.strip() + '\n'
    elif text_str and tag.name == u'h5':
      text_str = text_str.strip() + '\n'
    if text_str and text_str.strip() != '':
      text += text_str
  return text
  """
