# -*- coding: utf-8 -*-
"""Unit tests for the bdict.SanskritVocab module.

Tests the methods for building vocabuary from a Sanskrit document.
"""

import unittest

from bdict import ChinesePhrase


class ChinesePhraseTest(unittest.TestCase):

    def testExtractWords1(self):
        text = u'般'
        wdict = {}
        splitter = ChinesePhrase.ChinesePhraseSplitter(wdict)
        words = splitter.ExtractWords(text)
        self.assertEquals(1, len(words))
        self.assertEquals(text, words[0])

    def testExtractWords2(self):
        w1 = u'般'
        e1 = 'sort / kind / class / way / manner'
        w2 = u'若'
        e2 = 'to seem / to be like / as'
        text = w1 + w2
        wdict = {w1: e1, w2: e2}
        splitter = ChinesePhrase.ChinesePhraseSplitter(wdict)
        words = splitter.ExtractWords(text)
        self.assertEquals(2, len(words))
        self.assertEquals(w1, words[0])
        self.assertEquals(w2, words[1])

    def testIsCJKLetter(self):
        wdict = {}
        splitter = ChinesePhrase.ChinesePhraseSplitter(wdict)
        result = splitter.isCJKLetter(u'.')
        self.assertTrue(not result)

if __name__ == '__main__':
    unittest.main()
