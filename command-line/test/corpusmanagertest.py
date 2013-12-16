"""Unit tests for the bdict.corpusmanager module.

Tests the methods for loading the corpus file.
"""

import unittest

from bdict import corpusmanager


class CorpusManagerTest(unittest.TestCase):

    def testLoadCorpus(self):
        print('testLoadCorpus')
        manager = corpusmanager.CorpusManager()
        corpus = manager.LoadCorpus()
        self.assertTrue(corpus)
        self.assertTrue(len(corpus) > 0)
        self.assertEquals(corpus[0]['plain_text'], config['diamond-sutra-taisho.txt'])
