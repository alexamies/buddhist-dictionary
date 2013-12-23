# -*- coding: utf-8 -*-
"""Unit tests for the bdict.phrasematcher module.

Tests the methods for matching phrases against the phrase dataset.
"""
import unittest

from bdict import phrasematcher


class PhraseTest(unittest.TestCase):

    def testLoad(self):
        loader = PhraseLoader()
        loader.Load()


if __name__ == '__main__':
    unittest.main()
