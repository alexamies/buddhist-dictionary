# -*- coding: utf-8 -*-
"""Unit tests for the bdict.taggeddoc module.

Tests the methods for reading and analyzing documents with POS tags and gloss.
"""
import os.path
import unittest

from bdict import cedict
from bdict import taggeddoc


class TaggedDocTest(unittest.TestCase):

    def testLoadTaggedDoc1(self):
        filename = '../web/corpus/tagged/heart-sutra-xuanzang-tagged.txt'
        doc_analyzer = taggeddoc.TaggedDocumentAnalyzer()
        tagged_words = doc_analyzer.LoadTaggedDoc(filename)
        self.assertTrue(tagged_words)

    def testSaveWordSenseFreq1(self):
        corpus_entry = {'pos_tagged': 'heart-sutra-xuanzang-tagged.txt'}
        doc_analyzer = taggeddoc.TaggedDocumentAnalyzer()
        wfreq = doc_analyzer.WordSenseForCorpus()
        outfile = 'unigram_freq.txt'
        doc_analyzer.SaveWordSenseFreq(wfreq, outfile)
        self.assertTrue(os.path.isfile(outfile))

    def testWordSenseForCorpus1(self):
        doc_analyzer = taggeddoc.TaggedDocumentAnalyzer()
        wfreq = doc_analyzer.WordSenseForCorpus()
        self.assertTrue(wfreq)


if __name__ == '__main__':
    unittest.main()

