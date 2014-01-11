# -*- coding: utf-8 -*-
"""Unit tests for the bdict.unigram module.

Tests the methods for unigram part-of-speech tagging.
"""
import os.path
import unittest

from bdict import unigram


class UnigramTaggerTaggerTest(unittest.TestCase):

    def testLoadFreqTable(self):
        tagger = unigram.UnigramTagger()
        wfreq = tagger.LoadFreqTable()
        self.assertTrue(wfreq)
        key = u'須菩提'
        self.assertTrue(key in wfreq)

    def testMostFrequentWord1(self):
        tagger = unigram.UnigramTagger()
        traditional = u'是'
        word = tagger.MostFrequentWord(traditional)
        expected = u'17908'
        self.assertEqual(expected, word['id'])

    def testSaveWordSenseFreq(self):
        corpus_entry = {'pos_tagged': 'heart-sutra-xuanzang-tagged.txt'}
        tagger = unigram.UnigramTagger()
        wfreq = tagger.WordSenseFrequency(corpus_entry)
        outfile = 'unigram_heart_test.txt'
        tagger.SaveFreq(wfreq, outfile)
        self.assertTrue(os.path.isfile(outfile))

    def testWordSenseFrequency1(self):
        corpus_entry = {'pos_tagged': 'test-tagged.txt'}
        tagger = unigram.UnigramTagger()
        wfreq = tagger.WordSenseFrequency(corpus_entry)
        self.assertTrue(wfreq)
        self.assertEquals(5, len(wfreq))
        key = u'5047'
        self.assertTrue(key in wfreq)
        self.assertTrue(1, wfreq[key])

    def testWordSenseFrequency2(self):
        corpus_entry = {'pos_tagged': 'heart-sutra-xuanzang-tagged.txt'}
        tagger = unigram.UnigramTagger()
        wfreq = tagger.WordSenseFrequency(corpus_entry)
        self.assertTrue(wfreq)
        key = u'5047'
        self.assertTrue(key in wfreq)


if __name__ == '__main__':
    unittest.main()

