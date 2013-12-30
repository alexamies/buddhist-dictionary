# -*- coding: utf-8 -*-
"""Unit tests for the bdict.postaggeraccuracy module.

Tests the methods for building documents with English gloss and POS tags.
"""
import unittest

from bdict import postaggeraccuracy


class TaggerAccuracyTest(unittest.TestCase):

    def testTaggerAccuracy1(self):
        standard = [u'如是我聞']
        subject = [u'如是我聞']
        result = postaggeraccuracy.TaggerAccuracy(standard, subject)
        self.assertEqual(result, 1)

    def testTaggerAccuracy2(self):
        standard = [u'如是我聞', u'觀自在菩薩']
        subject = [u'如是我聞', u'行']
        result = postaggeraccuracy.TaggerAccuracy(standard, subject)
        self.assertEqual(result, 0.5)

    def testTaggerAccuracy3(self):
        filename1 = '../web/corpus/tagged/heart-sutra-xuanzang-tagged.txt'
        standard = postaggeraccuracy.LoadTaggedDoc(filename1)
        filename2 = '../web/corpus/tagged/heart-sutra-xuanzang-gen-tagged.txt'
        subject = postaggeraccuracy.LoadTaggedDoc(filename2)
        result = postaggeraccuracy.TaggerAccuracy(standard, subject)
        self.assertTrue(0 < result <= 1)

    def testLoadTaggedDoc1(self):
        filename = '../web/corpus/tagged/heart-sutra-xuanzang-gen-tagged.txt'
        tagged_words = postaggeraccuracy.LoadTaggedDoc(filename)
        self.assertTrue(tagged_words)


if __name__ == '__main__':
    unittest.main()

