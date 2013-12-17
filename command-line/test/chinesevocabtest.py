# -*- coding: utf-8 -*-
"""Unit tests for the bdict.chinesevocab module.

Tests the methods for building vocabuary from a Chinese document.
"""

import unittest

from bdict import app_exceptions
from bdict import chinesevocab


class ChineseVocabTest(unittest.TestCase):

    def testOpenDictionary(self):
        vocab = chinesevocab.ChineseVocabulary()
        wdict = vocab._OpenDictionary()
        self.assertTrue(wdict)
        self.assertTrue(len(wdict) > 0)
        w = u'賓頭廬尊者'
        self.assertTrue(w in wdict)

    def testBuildVocabulary1(self):
        try:
            corpus_entry = {}
            corpus_entry['plain_text'] = 'bogus.txt'
            vocab = chinesevocab.ChineseVocabulary()
            vocab.BuildVocabulary(corpus_entry)
        except app_exceptions.BDictException:
            pass
        else:
            self.assertFalse('Did not catch expected BDictException')

    def testBuildVocabulary2(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'diamond-sutra-taisho.txt'
        vocab = chinesevocab.ChineseVocabulary()
        vocab.BuildVocabulary(corpus_entry)


if __name__ == '__main__':
    unittest.main()
