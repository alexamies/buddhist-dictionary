# -*- coding: utf-8 -*-
"""Module to retrieve HTML web documents. =====================================

The HTML tags are stripped from the web documents to leave only the visible 
text.
"""
import re
from urllib import urlopen

from bs4 import BeautifulSoup

LEAVE_OUT = set([u'大藏經目錄', u'本經目錄', u'上一卷', u'下一卷'])

def readWebToPlainStrings(doc_url):
    """Returns the text of a web document as an array of strings.
    """
    html_doc = urlopen(doc_url).read()
    soup = BeautifulSoup(html_doc)
    return soup.stripped_strings

def readWebToPlainText(doc_url):
    """Returns the text of a web document as a single string.
    """
    html_doc = urlopen(doc_url).read()
    soup = BeautifulSoup(html_doc)
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    text = ''
    #for text_str in soup.strings:
    for tag in soup.find_all():
        text_str = tag.string
        #print(text_str)
        if text_str and tag.name == u'p':
            text_str = '<p>' + text_str.strip() + '</p>'
        elif text_str and tag.name == u'div':
            text_str = '<p>' + text_str.strip() + '</p>'
        elif tag.name == u'h1':
            continue
        elif text_str and tag.name == u'h2':
            text_str = '<h2>' + text_str.strip() + '</h2>'
        elif text_str and tag.name == u'h3':
            text_str = '<h3>' + text_str.strip() + '</h3>'
        elif text_str and tag.name == u'h4':
            text_str = '<h4>' + text_str.strip() + '</h4>'
        elif text_str and tag.name == u'h5':
            text_str = '<h5>' + text_str.strip() + '</h5>'
        if text_str and not text_str in LEAVE_OUT and text_str.strip() != '':
            text += text_str
    return text
