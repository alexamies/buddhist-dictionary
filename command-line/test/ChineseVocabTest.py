# -*- coding: utf-8 -*-
"""Unit tests for the bdict.SanskritVocab module.

Tests the methods for building vocabuary from a Sanskrit document.
"""

import unittest

from bdict import app_exceptions
from bdict import ChineseVocab


class ChineseVocabTest(unittest.TestCase):

    def testOpenDictionary(self):
        wdict = ChineseVocab._OpenDictionary()
        self.assertTrue(wdict)
        self.assertTrue(len(wdict) > 0)
        w = u'賓頭廬尊者'
        self.assertTrue(w in wdict)

    def testBuildVocabulary(self):
        try:
            ChineseVocab.BuildVocabulary('', '', 'testoutput.md')
        except app_exceptions.BDictException:
            pass
        else:
            self.assertFalse('Did not catch expected BDictException')


if __name__ == '__main__':
    unittest.main()
