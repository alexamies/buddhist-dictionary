# -*- coding: utf-8 -*-
"""Unit tests for the bdict.ngramfinder module.

Tests the methods for building n-grams from a text document.
"""
import unittest

from bdict import ngramfinder


class NGramFinderTest(unittest.TestCase):
    """Tests the NGramFinder class

    """

    def testNGramFinderBigram1(self):
        finder = ngramfinder.NGramFinder(2)
        words = [u'觀自在菩薩', u'行']
        for word in words:
            finder.AddWord(word)
        bigrams = finder.GetNGrams()
        self.assertTrue(2, len(bigrams))
        key = words[0] + words[1]
        keys = bigrams.keys()
        self.assertEqual(1, len(keys))
        self.assertEqual(key, keys[0])
        self.assertEqual(1, bigrams[keys[0]])

    def testNGramFinderBigram2(self):
        finder = ngramfinder.NGramFinder(2)
        words = [u'觀自在菩薩', u'行', u'深']
        for word in words:
            finder.AddWord(word)
        bigrams = finder.GetNGrams()
        self.assertTrue(2, len(bigrams))
        key0 = words[0] + words[1]
        key1 = words[1] + words[2]
        keys = bigrams.keys()
        self.assertEqual(2, len(bigrams))
        self.assertTrue(key0 in bigrams)
        self.assertEqual(1, bigrams[key0])
        self.assertTrue(key1 in bigrams)
        self.assertEqual(1, bigrams[key1])

    def testNGramFinderBigram3(self):
        finder = ngramfinder.NGramFinder(2)
        words = [u'觀自在菩薩', u'行', u'深', u'行', u'深']
        for word in words:
            finder.AddWord(word)
        bigrams = finder.GetNGrams()
        self.assertTrue(2, len(bigrams))
        key = words[1] + words[2]
        keys = bigrams.keys()
        self.assertEqual(2, bigrams[key])

    def testNGramFinderBigram4(self):
        finder = ngramfinder.NGramFinder(2)
        words = [u'觀自在菩薩', u'行', u'深', u'行', u'深']
        for word in words:
            finder.AddWord(word)
        bigrams = finder.GetNGrams(2)
        self.assertEqual(1, len(bigrams))

    def testNGramFinderTrigram1(self):
        finder = ngramfinder.NGramFinder(3)
        words = [u'四月', u'八', u'日', u'四月', u'八', u'日']
        for word in words:
            finder.AddWord(word)
        ngrams = finder.GetNGrams(2)
        bigram = u'八日'
        trigram = u'四月八日'
        self.assertTrue(bigram in ngrams)
        self.assertTrue(trigram in ngrams)
        self.assertEqual(2, ngrams[trigram])

    def testNGramFinder4gram1(self):
        finder = ngramfinder.NGramFinder(4)
        words = [u'太子', u'以', u'四月', u'八', u'日', u'以', u'四月', u'八', u'日']
        for word in words:
            finder.AddWord(word)
        ngrams = finder.GetNGrams(2)
        fourgram = u'以四月八日'
        self.assertTrue(fourgram in ngrams)
        self.assertEqual(2, ngrams[fourgram])

    def testNGramFinder5gram1(self):
        finder = ngramfinder.NGramFinder(5)
        words = [u'太子', u'以', u'四月', u'八', u'日', u'banana', u'太子', u'以', u'四月', u'八', u'日']
        for word in words:
            finder.AddWord(word)
        ngrams = finder.GetNGrams(2)
        fivegram = u'太子以四月八日'
        self.assertTrue(fivegram in ngrams)
        self.assertEqual(2, ngrams[fivegram])


if __name__ == '__main__':
    unittest.main()
