# -*- coding: utf-8 -*-
"""Unit tests for the bdict.bigram module.

Tests the bigram methods for part-of-speech tagging.
"""
import os.path
import unittest

from bdict import cedict
from bdict import bigram


class BigramTaggerTaggerTest(unittest.TestCase):

    def testLoadBigramFreq(self):
        tagger = bigram.BigramTagger()
        wfreq = tagger.LoadBigramFreq()

    def testWordSenseFrequency(self):
        tagger = bigram.BigramTagger()
        corpus_entry = {'pos_tagged': 'test-tagged.txt'}
        wfreq = tagger.WordSenseFrequency(corpus_entry)
        self.assertTrue(wfreq)

    def testSaveWordSenseFreq(self):
        corpus_entry = {'pos_tagged': 'heart-sutra-xuanzang-tagged.txt'}
        tagger = bigram.BigramTagger()
        wfreq = tagger.WordSenseFrequency(corpus_entry)
        outfile = 'bigram_heart_test.txt'
        tagger.SaveFreq(wfreq, outfile)
        self.assertTrue(os.path.isfile(outfile))


if __name__ == '__main__':
    unittest.main()

