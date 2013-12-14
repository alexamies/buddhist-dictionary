# -*- coding: utf-8 -*-
"""Unit tests for the bdict.SanskritVocab module.

Tests the methods for building vocabuary from a Sanskrit document.
"""

import unittest

from bdict import ChinesePhrase


class ChinesePhraseTest(unittest.TestCase):

    def testExtractWords(self):
        words = ChinesePhrase.ExtractWords()
        self.assertTrue(len(words) > 0)


if __name__ == '__main__':
    unittest.main()
