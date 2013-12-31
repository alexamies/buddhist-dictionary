# -*- coding: utf-8 -*-
"""Unit tests for the bdict.glossgenerator module.

Tests the methods for building HTML gloss document.
"""
import unittest

from bdict import glossgenerator


class GlossGeneratorTest(unittest.TestCase):

    def testGenerateDoc1(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'diamond-sutra-taisho.txt'
        start = u'如是我聞'
        corpus_entry['start'] = start
        end = u'本網站係採用'
        corpus_entry['end'] = end
        generator = glossgenerator.GlossGenerator()
        markup = generator.GenerateDoc(corpus_entry)
        self.assertTrue(markup)

    def testGenerateDoc2(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'diamond-sutra-taisho.txt'
        start = u'如是我聞'
        corpus_entry['start'] = start
        end = u'本網站係採用'
        corpus_entry['end'] = end
        generator = glossgenerator.GlossGenerator(output_type=glossgenerator.POS_TAGGED_TYPE)
        markup = generator.GenerateDoc(corpus_entry)
        self.assertTrue(markup)
        self.assertTrue(markup.find(u'如') == 0)

    def testWriteDoc1(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'heart-sutra-xuanzang.txt'
        start = u'觀自在菩薩行深'
        corpus_entry['start'] = start
        end = u'本網站係採用'
        corpus_entry['end'] = end
        generator = glossgenerator.GlossGenerator(output_type=glossgenerator.POS_TAGGED_TYPE)
        generator.WriteDoc(corpus_entry)


if __name__ == '__main__':
    unittest.main()

