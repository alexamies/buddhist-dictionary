# -*- coding: utf-8 -*-
"""Unit tests for the bdict.ngramfinder module.

Tests the methods for building n-grams from a text document.
"""
import unittest

from bdict import ngramfinder


class NGramFinderTest(unittest.TestCase):
    """Tests the NGramFinder class

    """

    def testNGramFinder1(self):
        finder = ngramfinder.NGramFinder(2)
        words = [u'觀自在菩薩', u'行']
        for word in words:
            finder.AddWord(word)
        bigrams = finder.GetNGrams()
        self.assertTrue(2, len(bigrams))
        key = words[0] + words[1]
        keys = bigrams.keys()
        self.assertTrue(key, keys[0])
        self.assertTrue(1, bigrams[keys[0]])

    def testNGramFinder2(self):
        finder = ngramfinder.NGramFinder(2)
        words = [u'觀自在菩薩', u'行', u'深']
        for word in words:
            finder.AddWord(word)
        bigrams = finder.GetNGrams()
        self.assertTrue(2, len(bigrams))
        key0 = words[0] + words[1]
        key1 = words[1] + words[2]
        keys = bigrams.keys()
        self.assertTrue(1, bigrams[key0])
        self.assertTrue(1, bigrams[key1])

    def testNGramFinder3(self):
        finder = ngramfinder.NGramFinder(2)
        words = [u'觀自在菩薩', u'行', u'深', u'行', u'深']
        for word in words:
            finder.AddWord(word)
        bigrams = finder.GetNGrams()
        self.assertTrue(2, len(bigrams))
        key = words[1] + words[2]
        keys = bigrams.keys()
        self.assertTrue(2, bigrams[key])

    def testNGramFinder4(self):
        finder = ngramfinder.NGramFinder(2)
        words = [u'觀自在菩薩', u'行', u'深', u'行', u'深']
        for word in words:
            finder.AddWord(word)
        bigrams = finder.GetNGrams(2)
        self.assertTrue(1, len(bigrams))

