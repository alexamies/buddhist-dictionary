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

    def testGenerateDoc3(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'http://www.cbeta.org/result/normal/T50/2059_008.htm'
        corpus_entry['type'] = 'web'
        start = u'三年也。'
        corpus_entry['start'] = start
        end = u'釋曇度。本姓蔡。'
        corpus_entry['end'] = end
        generator = glossgenerator.GlossGenerator()
        markup = generator.GenerateDoc(corpus_entry)
        self.assertTrue(markup)
        expected = u'a final modal particle'
        self.assertTrue(markup.find(expected) > 0)
        # self.assertEqual(expected, markup)

    def testWriteDoc1(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'heart-sutra-xuanzang.txt'
        start = u'觀自在菩薩行深'
        corpus_entry['start'] = start
        end = u'本網站係採用'
        corpus_entry['end'] = end
        generator = glossgenerator.GlossGenerator(output_type=glossgenerator.POS_TAGGED_TYPE)
        generator.WriteDoc(corpus_entry)

    def testWord1(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'heart-sutra-xuanzang.txt'
        start = u'觀自在菩薩行深'
        corpus_entry['start'] = start
        end = u'本網站係採用'
        corpus_entry['end'] = end
        generator = glossgenerator.GlossGenerator()
        element_text = u'也'
        entry_id = u'8853'
        entry = {'grammar': 'particle', 'traditional': element_text}
        url = u'/buddhistdict/word_detail.php?id=%s' % entry_id
        title = u'yě | a final modal particle indicating certainy or decision'
        expected = u'<a href="%s" title="%s">%s</a>' % (url, title, element_text)
        link = generator._Word(element_text, entry)
        self.assertEqual(expected, link)


if __name__ == '__main__':
    unittest.main()

