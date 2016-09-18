# -*- coding: utf-8 -*-
"""
Utility for aggregating metadata from the Korean Buddhist Canon. 
Metadata is located in directory ../data/corpus/korean
"""

import csv

# Taisho-Korean index
INDEX_FILE_NAME = '../data/corpus/korean/taisho-korean-index.txt'
tkindex = {}


def loadindex():
  """
  Reads the index into memory
  """
  with open(INDEX_FILE_NAME, 'r') as f:
    indexreader = csv.reader(f, delimiter='\t')
    for row in indexreader:
      if len(row) == 2:
        tkindex[row[0]] = row[1]
  return tkindex  


def getkoreanid(tid):
  """
  Get the id of the entry in the Korean canon matching the given Taisho id.

  If there is no matching id in the Korean canon return "0".
  """
  if tid in tkindex:
  	return tkindex[tid]
  return "0"


tkindex = loadindex()