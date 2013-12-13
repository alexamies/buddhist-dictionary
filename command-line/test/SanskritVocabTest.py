# -*- coding: utf-8 -*-

import unittest
import sys, os

from bdict import SanskritVocab

TARGET_TEST_DIR = '..'

sys.path.insert(0, os.path.dirname(TARGET_TEST_DIR))


class SanskritVocabTest(unittest.TestCase):

    def testStripPunctuation1(self):
        token = 'sādhu'
        word = SanskritVocab._StripPunctuation(token)
        expected = 'sādhu'
        self.assertEquals(expected, token)

    def testStripPunctuation2(self):
        token = 'sādhu|'
        word = SanskritVocab._StripPunctuation(token)
        expected = 'sādhu'
        self.assertEquals(expected, token)

    def testStripPunctuation3(self):
        token = '!Hello.'
        word = SanskritVocab._StripPunctuation(token)
        expected = 'Hello'
        self.assertEquals(expected, token)

if __name__ == '__main__':
    unittest.main()
