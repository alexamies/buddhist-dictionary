# -*- coding: utf-8 -*-
"""Unit tests for the bdict.taggeddoc module.

Tests the methods for reading and analyzing documents with POS tags and gloss.
"""
import os.path
import unittest

from bdict import cedict
from bdict import taggeddoc


class TaggedDocTest(unittest.TestCase):

    def testWordSenseForCorpus(self):
        doc_analyzer = taggeddoc.TaggedDocumentAnalyzer()
        results = doc_analyzer.WordSenseForCorpus()
        self.assertTrue(results[0])
        self.assertTrue(results[1])
        self.assertTrue(results[2])


if __name__ == '__main__':
    unittest.main()

