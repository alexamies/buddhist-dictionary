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
    for text_str in soup.strings:
        if not text_str in LEAVE_OUT and text_str.strip() != '':
            text += text_str
    return text
