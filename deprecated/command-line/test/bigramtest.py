# -*- coding: utf-8 -*-
"""Unit tests for the bdict.bigram module.

Tests the bigram methods for part-of-speech tagging.
"""
import os.path
import unittest

from bdict import cedict
from bdict import bigram


class BigramTaggerTaggerTest(unittest.TestCase):

    def testLoadFreqTable(self):
        tagger = bigram.BigramTagger()
        wfreq = tagger.LoadFreqTable()
        self.assertTrue(wfreq)
        previous_text = u'以'
        element_text = u'故'
        key = previous_text, element_text
        self.assertTrue(key in wfreq)

    def testMostFrequentWord1(self):
        tagger = bigram.BigramTagger()
        previous_text = u'以'
        element_text = u'故'
        word = tagger.MostFrequentWord(previous_text, element_text)
        expected = u'7115'
        self.assertEqual(expected, word['id'])

    def testSaveWordSenseFreq(self):
        corpus_entry = {'pos_tagged': 'heart-sutra-xuanzang-tagged.txt'}
        tagger = bigram.BigramTagger()
        wfreq = tagger.WordSenseFrequency(corpus_entry)
        outfile = 'bigram_heart_test.txt'
        tagger.SaveFreq(wfreq, outfile)
        self.assertTrue(os.path.isfile(outfile))

    def testWordSenseFrequency(self):
        tagger = bigram.BigramTagger()
        corpus_entry = {'pos_tagged': 'test-tagged.txt'}
        wfreq = tagger.WordSenseFrequency(corpus_entry)
        self.assertTrue(wfreq)


if __name__ == '__main__':
    unittest.main()

