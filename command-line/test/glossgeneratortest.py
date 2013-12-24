# -*- coding: utf-8 -*-
"""Unit tests for the bdict.glossgenerator module.

Tests the methods for building HTML gloss document.
"""
import unittest

from bdict import glossgenerator


class HTMLGlossGeneratorTest(unittest.TestCase):

    def testGenerateDoc(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'diamond-sutra-taisho.txt'
        start = u'如是我聞'
        corpus_entry['start'] = start
        end = u'本網站係採用'
        corpus_entry['end'] = end
        generator = glossgenerator.HTMLGlossGenerator()
        html = generator.GenerateDoc(corpus_entry)
        self.assertTrue(html)


if __name__ == '__main__':
    unittest.main()

