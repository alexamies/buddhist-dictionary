# -*- coding: utf-8 -*-
"""Unit tests for the bdict.taggeddoc module.

Tests the methods for reading and analyzing documents with POS tags and gloss.
"""
import os.path
import unittest

from bdict import taggeddoc


class TaggedDocTest(unittest.TestCase):

    def testLoadTaggedDoc1(self):
        filename = '../web/corpus/tagged/heart-sutra-xuanzang-tagged.txt'
        tagged_words = taggeddoc.LoadTaggedDoc(filename)
        self.assertTrue(tagged_words)

    def testSaveWordSenseFreq1(self):
        infile = '../web/corpus/tagged/heart-sutra-xuanzang-tagged.txt'
        wfreq = taggeddoc.WordSenseFrequency(infile)
        outfile = 'unigram_freq.txt'
        taggeddoc.SaveWordSenseFreq(wfreq, outfile)
        self.assertTrue(os.path.isfile(outfile))

    def testWordSenseFrequency1(self):
        filename = '../web/corpus/tagged/heart-sutra-xuanzang-tagged.txt'
        wfreq = taggeddoc.WordSenseFrequency(filename)
        self.assertTrue(wfreq)

    def testParseLine1(self):
        line = u'咒/NN[zhòu | mantra]'
        wfreq_entry = taggeddoc._ParseLine(line)
        self.assertEqual(u'咒', wfreq_entry['element_text'])
        self.assertEqual(u'NN', wfreq_entry['tag'])
        self.assertEqual(u'mantra', wfreq_entry['english'])


if __name__ == '__main__':
    unittest.main()

