# -*- coding: utf-8 -*-
"""Unit tests for the bdict.bigram module.

Tests the bigram methods for part-of-speech tagging.
"""
import os.path
import unittest

from bdict import cedict
from bdict import bigram


class BigramTaggerTaggerTest(unittest.TestCase):

    def testLoadBigramFreq(self):
        tagger = bigram.BigramTagger()
        wfreq = tagger.LoadBigramFreq()


if __name__ == '__main__':
    unittest.main()

