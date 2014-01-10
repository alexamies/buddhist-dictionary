# -*- coding: utf-8 -*-
"""Unit tests for the bdict.unigram module.

Tests the methods for unigram part-of-speech tagging.
"""
import os.path
import unittest

from bdict import cedict
from bdict import unigram


class UnigramTaggerTaggerTest(unittest.TestCase):

    def testLoadUnigramFreq(self):
        tagger = unigram.UnigramTagger()
        wfreq = tagger.LoadUnigramFreq()
        self.assertTrue(wfreq)
        key = u'須菩提'
        self.assertTrue(key in wfreq)

    def testMostFrequentWord1(self):
        tagger = unigram.UnigramTagger()
        traditional = u'是'
        word = tagger.MostFrequentWord(traditional)
        expected = u'17908'
        self.assertEqual(expected, word['id'])

    def testSaveWordSenseFreq1(self):
        corpus_entry = {'pos_tagged': 'heart-sutra-xuanzang-tagged.txt'}
        tagger = unigram.UnigramTagger()
        wfreq = tagger.WordSenseFrequency(corpus_entry)
        outfile = 'unigram_test.txt'
        tagger.SaveUnigramFreq(wfreq, outfile)
        self.assertTrue(os.path.isfile(outfile))

    def testWordSenseFrequency1(self):
        corpus_entry = {'pos_tagged': 'heart-sutra-xuanzang-tagged.txt'}
        tagger = unigram.UnigramTagger()
        wfreq = tagger.WordSenseFrequency(corpus_entry)
        self.assertTrue(wfreq)

    def testGetBestWordSense1(self):
        dictionary = cedict.ChineseEnglishDict()
        wdict = dictionary.OpenDictionary() # Word dictionary
        line = u'咒/NN[zhòu | mantra]'
        wfreq_entry = {'tagged_text': line,
                       'element_text': u'咒',
                       'tag': 'NN',
                       'english': 'mantra'
                      }
        word_entry = unigram._GetBestWordSense(wdict, wfreq_entry)
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
        word_entry = unigram._GetBestWordSense(wdict, wfreq_entry)
        self.assertEqual(u'anuttara-samyak-sambodhi / anuttara samyaksaṃbodhi / anuttarasamyaksaṃbodhi', 
                         word_entry['english'])


if __name__ == '__main__':
    unittest.main()

