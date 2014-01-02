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
        tagged_words = taggeddoc.LoadTaggedDoc(filename)
        self.assertTrue(tagged_words)

    def testSaveWordSenseFreq1(self):
        corpus_entry = {'pos_tagged': 'heart-sutra-xuanzang-tagged.txt'}
        wfreq = taggeddoc.WordSenseFrequency(corpus_entry)
        outfile = 'unigram_freq.txt'
        taggeddoc.SaveWordSenseFreq(wfreq, outfile)
        self.assertTrue(os.path.isfile(outfile))

    def testWordSenseFrequency1(self):
        corpus_entry = {'pos_tagged': 'heart-sutra-xuanzang-tagged.txt'}
        wfreq = taggeddoc.WordSenseFrequency(corpus_entry)
        self.assertTrue(wfreq)

    def testParseLine1(self):
        line = u'咒/NN[zhòu | mantra]'
        wfreq_entry = taggeddoc._ParseLine(line)
        self.assertEqual(u'咒', wfreq_entry['element_text'])
        self.assertEqual(u'NN', wfreq_entry['tag'])
        self.assertEqual(u'mantra', wfreq_entry['english'])

    def testGetBestWordSense1(self):
        dictionary = cedict.ChineseEnglishDict()
        wdict = dictionary.OpenDictionary() # Word dictionary
        line = u'咒/NN[zhòu | mantra]'
        wfreq_entry = {'tagged_text': line,
                       'element_text': u'咒',
                       'tag': 'NN',
                       'english': 'mantra'
                      }
        word_entry = taggeddoc._GetBestWordSense(wdict, wfreq_entry)
        self.assertEqual(u'mantra', word_entry['english'])

    def testGetBestWordSense2(self):
        dictionary = cedict.ChineseEnglishDict()
        wdict = dictionary.OpenDictionary() # Word dictionary
        line = u'阿耨多羅三藐三菩提/NN[ānòuduōluó sānmiǎo sānpútí | anuttara samyaksaṃbodhi]'
        wfreq_entry = {'tagged_text': line,
                       'element_text': u'阿耨多羅三藐三菩提',
                       'tag': 'NN',
                       'english': u'anuttara samyaksaṃbodhi'
                      }
        word_entry = taggeddoc._GetBestWordSense(wdict, wfreq_entry)
        self.assertEqual(u'anuttara-samyak-sambodhi / anuttara samyaksaṃbodhi / anuttarasamyaksaṃbodhi', 
                         word_entry['english'])

    def testWordSenseForCorpus1(self):
        wfreq = taggeddoc.WordSenseForCorpus()
        self.assertTrue(wfreq)


if __name__ == '__main__':
    unittest.main()

