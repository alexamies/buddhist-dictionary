# -*- coding: utf-8 -*-
"""Unit tests for the bdict.SanskritVocab module.

Tests the methods for building vocabuary from a Sanskrit document.
"""

import unittest

from bdict import ChineseVocab

TARGET_TEST_DIR = '..'

sys.path.insert(0, os.path.dirname(TARGET_TEST_DIR))


class ChineseVocabTest(unittest.TestCase):

    def testOpenDictionary(self):
        sdict = SanskritVocab._OpenDictionary()
        self.assertTrue(sdict)

    def testStripPunctuation1(self):
        token = u'sādhu'
        word = SanskritVocab._StripPunctuation(token)
        expected = u'sādhu'
        self.assertEquals(expected, word)

    def testStripPunctuation2(self):
        token = 'Hello|'
        word = SanskritVocab._StripPunctuation(token)
        expected = 'Hello'
        self.assertEquals(expected, word)

    def testStripPunctuation3(self):
        token = 'nādharmaḥ|'
        word = SanskritVocab._StripPunctuation(token)
        expected = 'nādharmaḥ'
        self.assertEquals(expected, word)

    def testStripPunctuation4(self):
        token = 'vadet-'
        word = SanskritVocab._StripPunctuation(token)
        expected = 'vadet'
        self.assertEquals(expected, word)

    def testStripPunctuation5(self):
        token = 'iti||6||'
        word = SanskritVocab._StripPunctuation(token)
        expected = 'iti'
        self.assertEquals(expected, word)

    def testStripPunctuation6(self):
        token = '()'
        word = SanskritVocab._StripPunctuation(token)
        expected = ''
        self.assertEquals(expected, word)

    def testConvertNonStandard1(self):
        token = 'śayyāṁ'
        word = SanskritVocab._ConvertNonStandard(token)
        expected = 'śayyāṃ'
        self.assertEquals(expected, word)


if __name__ == '__main__':
    unittest.main()
