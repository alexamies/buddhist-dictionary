# -*- coding: utf-8 -*-
"""Unit tests for the bdict.cjktextreader module.

Tests the methods for reading the text file into a sequence of characters.
"""
import os.path
import unittest

from bdict import app_exceptions
from bdict import cjktextreader


class CJKTextReaderTest(unittest.TestCase):

    def testReadText1(self):
        try:
            corpus_entry = {}
            corpus_entry['plain_text'] = 'bogus.txt'
            reader = cjktextreader.CJKTextReader()
            reader.ReadText(corpus_entry)
        except app_exceptions.BDictException:
            pass
        else:
            self.assertFalse('Did not catch expected BDictException')

    def testReadText2(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'diamond-sutra-taisho.txt'
        start = u'如是我聞'
        corpus_entry['start'] = start
        end = u'本網站係採用'
        corpus_entry['end'] = end
        reader = cjktextreader.CJKTextReader()
        characters = reader.ReadText(corpus_entry)
        self.assertTrue(characters)
        self.assertEquals(0, characters.find(start))
        self.assertEquals(-1, characters.find(end))
        ascii = u'T'
        self.assertEquals(-1, characters.find(ascii))
        punctuation = u'，'
        self.assertTrue(-1 < characters.find(punctuation))

    def testReadText3(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'abhiniskramana-scroll1-taisho.txt'
        start = u'太子以四月八日'
        corpus_entry['start'] = start
        end = u'本網站係採用'
        corpus_entry['end'] = end
        reader = cjktextreader.CJKTextReader()
        characters = reader.ReadText(corpus_entry)
        self.assertTrue(characters)
        self.assertEquals(0, characters.find(start))
        self.assertEquals(-1, characters.find(end))
        ascii = u'T'
        self.assertEquals(-1, characters.find(ascii))
        punctuation = u'，'
        self.assertTrue(-1 < characters.find(punctuation))

    def testReadText4(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'guanxifo-scroll1-taisho.txt'
        start = u'以四月八日夜半'
        corpus_entry['start'] = start
        end = u'諸善男子善女人'
        corpus_entry['end'] = end
        reader = cjktextreader.CJKTextReader()
        characters = reader.ReadText(corpus_entry)
        self.assertTrue(characters)
        self.assertEquals(0, characters.find(start))
        self.assertEquals(-1, characters.find(end))
        last = u'正是佛生之日。'
        self.assertTrue(-1 < characters.find(last))

    def testReadWholeText1(self):
        corpus_entry = {}
        corpus_entry['plain_text'] = 'diamond-sutra-taisho.txt'
        reader = cjktextreader.CJKTextReader()
        text = reader.ReadWholeText(corpus_entry)
        self.assertTrue(text)
        start = u'【經錄部類】'
        self.assertEquals(0, text.find(start))


if __name__ == '__main__':
    unittest.main()

