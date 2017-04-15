# -*- coding: utf-8 -*-
"""Unit tests for the bdict.phrasematcher module.

Tests the methods for matching phrases against the phrase dataset.
"""
import unittest

from bdict import phrasematcher


class PhraseTest(unittest.TestCase):

    def testLoad1(self):
        dataset = phrasematcher.PhraseDataset()
        phrases = dataset.Load()
        self.assertTrue(phrases)
        self.assertTrue(u'乘白象' in phrases)

    def testLoad2(self):
        dataset = phrasematcher.PhraseDataset()
        phrases = dataset.Load()
        self.assertTrue(phrases)
        self.assertTrue(u'何以故' in phrases)

    def testMatches1(self):
        dataset = phrasematcher.PhraseDataset()
        dataset.Load()
        text = u'乘白象'
        matches = dataset.Matches(text)
        self.assertEquals(1, len(matches))
        match = matches[0]
        self.assertEquals(text, match['chinese_phrase'])

    def testMatches2(self):
        dataset = phrasematcher.PhraseDataset()
        dataset.Load()
        self.assertFalse(dataset.Matches(u'baluga'))

    def testMatches3(self):
        words = [u'彈琴', u'乘白象']
        text = words[0] + words[1]
        dataset = phrasematcher.PhraseDataset()
        dataset.Load()
        matches = dataset.Matches(text)
        self.assertEquals(2, len(matches))

    def testMatches4(self):
        words = [u'彈琴', u'banana', u'乘白象']
        text = words[0] + words[2] + words[1]
        dataset = phrasematcher.PhraseDataset()
        dataset.Load()
        matches = dataset.Matches(text)
        self.assertEquals(2, len(matches))

if __name__ == '__main__':
    unittest.main()
