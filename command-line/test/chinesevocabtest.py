# -*- coding: utf-8 -*-
"""Unit tests for the bdict.chinesevocab module.

Tests the methods for building vocabuary from a Chinese document.
"""
import os.path
import unittest

from bdict import app_exceptions
from bdict import chinesevocab
from bdict import configmanager


class ChineseVocabTest(unittest.TestCase):

    def testBuildVocabulary1(self):
        try:
            corpus_entry = {}
            corpus_entry['plain_text'] = 'bogus.txt'
            vocab = chinesevocab.ChineseVocabulary()
            vocab.BuildVocabulary(corpus_entry)
        except app_exceptions.BDictException:
            pass
        else:
            self.assertFalse('Did not catch expected BDictException')

    def testBuildVocabulary2(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'heart-sutra-xuanzang.txt'
        corpus_entry['start'] = u'觀自在菩薩行深'
        corpus_entry['end'] = u'本網站係採用'
        corpus_entry['source_name'] = u'Prajñāpāramitā Heart Sūtra 般若波羅蜜多心經'
        corpus_entry['source'] = u'Taisho Tripitaka'
        corpus_entry['reference'] = u'Vol. 8, No. 251'
        corpus_entry['translator'] = u'Xuanzang'
        corpus_entry['type'] = 'file'
        vocab = chinesevocab.ChineseVocabulary()
        vocab.BuildVocabulary(corpus_entry)
        manager = configmanager.ConfigurationManager()
        self.config = manager.LoadConfig()
        directory = self.config['corpus_directory']
        fullpath = '%s/%s' % (directory, chinesevocab.DEFAULT_OUTFILE)
        self.assertTrue(os.path.isfile(fullpath))


if __name__ == '__main__':
    unittest.main()
