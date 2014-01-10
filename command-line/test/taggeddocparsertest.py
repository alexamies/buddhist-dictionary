# -*- coding: utf-8 -*-
"""Unit tests for the bdict.unigram module.

Tests the methods for unigram part-of-speech tagging.
"""
import unittest

from bdict import taggeddocparser


class UnigramTaggerTaggerTest(unittest.TestCase):


    def testParseLine1(self):
        line = u'咒/NN[zhòu | mantra]'
        wfreq_entry = taggeddocparser.ParseLine(line)
        self.assertEqual(u'咒', wfreq_entry['element_text'])
        self.assertEqual(u'NN', wfreq_entry['tag'])
        self.assertEqual(u'mantra', wfreq_entry['english'])


if __name__ == '__main__':
    unittest.main()

