# -*- coding: utf-8 -*-
"""
Utility for aggregating metadata from the Taisho Buddhist Canon. 
"""

import urllib2


def geturl(volume, tid):
  """
  Get the URL of the entry in the Taisho matching the given Taisho id.

  Also, check that the URL is correct by doing a GET.
  """
  url = "http://tripitaka.cbeta.org/T%dn0%s" % (volume, tid)
  response = urllib2.urlopen(url)  
  return url