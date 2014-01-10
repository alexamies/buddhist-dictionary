# -*- coding: utf-8 -*-
"""Unit tests for the bdict.postaggeraccuracy module.

Tests the methods for testing accuracy of tagged documents with English gloss and POS tags.
"""
import unittest

from bdict import glossgenerator
from bdict import postaggeraccuracy
from bdict import taggeddoc


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
        corpus_entry = {}
        corpus_entry['plain_text'] = 'heart-sutra-xuanzang.txt'
        corpus_entry['start'] = u'觀自在菩薩行深'
        corpus_entry['end'] = u'本網站係採用'
        corpus_entry['source_name'] = u'Prajñāpāramitā Heart Sūtra 般若波羅蜜多心經'
        corpus_entry['source'] = u'Taisho Tripitaka'
        corpus_entry['reference'] = u'Vol. 8, No. 251'
        corpus_entry['translator'] = u'Xuanzang'
        generator = glossgenerator.GlossGenerator(output_type=glossgenerator.POS_TAGGED_TYPE)
        filename = generator.WriteDoc(corpus_entry)
        filename1 = '../web/corpus/tagged/heart-sutra-xuanzang-tagged.txt'
        doc_analyzer = taggeddoc.TaggedDocumentAnalyzer()
        standard = doc_analyzer.LoadTaggedDoc(filename1)
        subject = doc_analyzer.LoadTaggedDoc(filename)
        result = postaggeraccuracy.TaggerAccuracy(standard, subject)
        self.assertTrue(0 < result <= 1)


if __name__ == '__main__':
    unittest.main()

