# -*- coding: utf-8 -*-
"""
Tests utility for Korean canon metadata management
"""

from korean import getkoreanid


def main():
  kid = getkoreanid("490")
  print "Got kid %s: " % kid


if __name__ == "__main__": main()