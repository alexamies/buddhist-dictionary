# -*- coding: utf-8 -*-
"""Unit tests for the bdict.SanskritVocab module.

Tests the methods for building vocabuary from a Sanskrit document.
"""
import unicodedata
import unittest

from bdict import ChinesePhrase


class ChinesePhraseTest(unittest.TestCase):

    def testExtractWords1(self):
        w1 = u'般'
        # print('testExtractWords1 : c1: %s' % unicodedata.name(w1))
        text = w1
        wdict = {}
        splitter = ChinesePhrase.ChinesePhraseSplitter(wdict)
        words = splitter.ExtractWords(text)
        self.assertEquals(1, len(words))
        self.assertEquals(w1, words[0])

    def testExtractWords2(self):
        w1 = u'般'
        e1 = 'sort / kind / class / way / manner'
        w2 = u'若'
        e2 = 'to seem / to be like / as'
        # print('testExtractWords2 : w1: %s, w2: %s' % (unicodedata.name(w1), unicodedata.name(w2)))
        text = w1 + w2
        wdict = {w1: e1, w2: e2}
        splitter = ChinesePhrase.ChinesePhraseSplitter(wdict)
        words = splitter.ExtractWords(text)
        self.assertEquals(2, len(words))
        self.assertEquals(w1, words[0])
        self.assertEquals(w2, words[1])

    def testExtractWords3(self):
        w1 = u'時'
        e1 = 'time'
        w2 = u'，'
        # print('testExtractWords3 : w1: %s, w2: %s' % (unicodedata.name(w1), unicodedata.name(w2)))
        text = w1 + w2
        wdict = {w1: e1}
        splitter = ChinesePhrase.ChinesePhraseSplitter(wdict)
        words = splitter.ExtractWords(text)
        self.assertEquals(1, len(words))
        self.assertEquals(w1, words[0])
        print('\n')

    def testExtractWords4(self):
        w1 = u'般'
        e1 = 'sort / kind / class / way / manner'
        w2 = u'，'
        e2 = 'CJK comma'
        w3 = u'若'
        e3 = 'to seem / to be like / as'
        # print('testExtractWords4 : w1: %s, w3: %s' % (unicodedata.name(w1), unicodedata.name(w3)))
        text = w1 + w2 + w3
        wdict = {w1: e1, w3: e3}
        splitter = ChinesePhrase.ChinesePhraseSplitter(wdict)
        words = splitter.ExtractWords(text)
        self.assertEquals(2, len(words))
        self.assertEquals(w1, words[0])
        self.assertEquals(w3, words[1])
        print('\n')

    def testExtractWords5(self):
        w1 = u'如是我聞' # 0-3
        e1 = 'Thus I heard'
        w2 = u'：'       # 4
        e2 = 'colon'
        w3 = u'　'       # 5
        e3 = 'space'
        w4 = u'一時'     # 6-7
        e4 = 'one time'
        w5 = u'，'       # 8
        e5 = 'comma'
        w6 = u'佛'       # 9
        e6 = 'Buddha'
        w7 = u'在'       # 10
        e7 = 'at'
        w8 = u'舍衛國'   # 11-13
        e8 = 'Sravasti'
        print('testExtractWords5')
        text = w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8
        wdict = {w1: e1, w4: e4, w6: e6, w7: e7, w8: e8}
        self.assertTrue(w1 in wdict)
        self.assertEquals(14, len(text))
        splitter = ChinesePhrase.ChinesePhraseSplitter(wdict)
        words = splitter.ExtractWords(text)
        self.assertEquals(5, len(words))
        self.assertEquals(w1, words[0])
        self.assertEquals(w4, words[1])
        self.assertEquals(w6, words[2])
        self.assertEquals(w7, words[3])
        self.assertEquals(w8, words[4])
        print('\n')

    def testExtractWords6(self):
        w1 = u'如是我聞' # 0-3
        e1 = 'Thus I heard'
        w2 = u'：'       # 4
        e2 = 'colon'
        w3 = u'　'       # 5
        e3 = 'space'
        w4 = u'一時'     # 6-7
        e4 = 'one time'
        w5 = u'，'       # 8
        e5 = 'comma'
        w6 = u'佛'       # 9
        e6 = 'Buddha'
        w7 = u'在'       # 10
        e7 = 'at'
        w8 = u'舍衛國'   # 11-13
        e8 = 'Sravasti'
        print('testExtractWords5')
        text = w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8
        wdict = {}
        self.assertEquals(14, len(text))
        splitter = ChinesePhrase.ChinesePhraseSplitter(wdict)
        words = splitter.ExtractWords(text)
        self.assertEquals(11, len(words))
        self.assertEquals(w1[0], words[0])
        self.assertEquals(w1[1], words[1])
        self.assertEquals(w1[2], words[2])
        self.assertEquals(w1[3], words[3])
        self.assertEquals(w4[0], words[4])
        self.assertEquals(w4[1], words[5])
        self.assertEquals(w6, words[6])
        self.assertEquals(w7, words[7])
        self.assertEquals(w8[0], words[8])
        self.assertEquals(w8[1], words[9])
        self.assertEquals(w8[2], words[10])
        print('\n')

    def testIsCJKLetter1(self):
        c = u'.'
        splitter = ChinesePhrase.ChinesePhraseSplitter( {})
        print('cat: %s : name: %s' % (unicodedata.category(c), unicodedata.name(c)))
        result = splitter.isCJKLetter(c)
        self.assertFalse(result)

    def testIsCJKLetter2(self):
        c = u'般'
        splitter = ChinesePhrase.ChinesePhraseSplitter( {})
        print('cat: %s : name: %s' % (unicodedata.category(c), unicodedata.name(c)))
        result = splitter.isCJKLetter(c)
        self.assertTrue(result)

    def testIsCJKLetter3(self):
        splitter = ChinesePhrase.ChinesePhraseSplitter({})
        c = u'。'
        print('cat: %s : name: %s' % (unicodedata.category(c), unicodedata.name(c)))
        result = splitter.isCJKLetter(c)
        self.assertFalse(result)

    def testIsCJKLetter4(self):
        c = u'！'
        splitter = ChinesePhrase.ChinesePhraseSplitter( {})
        print('cat: %s : name: %s' % (unicodedata.category(c), unicodedata.name(c)))
        result = splitter.isCJKLetter(c)
        self.assertFalse(result)

    def testIsCJKLetter5(self):
        c = u'「'
        splitter = ChinesePhrase.ChinesePhraseSplitter( {})
        print('cat: %s : name: %s' % (unicodedata.category(c), unicodedata.name(c)))
        result = splitter.isCJKLetter(c)
        self.assertFalse(result)

    def testIsCJKLetter6(self):
        c = u'T'
        splitter = ChinesePhrase.ChinesePhraseSplitter( {})
        print('cat: %s : name: %s' % (unicodedata.category(c), unicodedata.name(c)))
        result = splitter.isCJKLetter(c)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
