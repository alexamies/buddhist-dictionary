# -*- coding: utf-8 -*-
"""Unit tests for the bdict.unigram module.

Tests the methods for unigram part-of-speech tagging.
"""
import unittest

from bdict import cedict
from bdict import taggeddocparser


class TaggedDocParserTest(unittest.TestCase):

    def testLoadTaggedDoc1(self):
        filename = '../web/corpus/tagged/heart-sutra-xuanzang-tagged.txt'
        tagged_words = taggeddocparser.LoadTaggedDoc(filename)
        self.assertTrue(tagged_words)

    def testParseLine1(self):
        line = u'咒/NN[zhòu | mantra]'
        wfreq_entry = taggeddocparser.ParseLine(line)
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
        word_entry = taggeddocparser.GetBestWordSense(wdict, wfreq_entry)
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
        word_entry = taggeddocparser.GetBestWordSense(wdict, wfreq_entry)
        self.assertEqual(u'anuttara-samyak-sambodhi / anuttara samyaksaṃbodhi / anuttarasamyaksaṃbodhi', 
                         word_entry['english'])


if __name__ == '__main__':
    unittest.main()

