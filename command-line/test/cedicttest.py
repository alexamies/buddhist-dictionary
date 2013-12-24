# -*- coding: utf-8 -*-
"""Unit tests for the bdict.chinesevocab module.

Tests the methods for building vocabuary from a Chinese document.
"""
import unittest

from bdict import cedict


class CEDictTest(unittest.TestCase):

    def testOpenDictionary(self):
        dictionary = cedict.ChineseEnglishDict()
        wdict = dictionary.OpenDictionary()
        self.assertTrue(wdict)
        self.assertTrue(len(wdict) > 0)
        w = u'賓頭廬尊者'
        self.assertTrue(w in wdict)

    def testIsFunctionWord1(self):
        word = {'traditional': u'者', 'grammar': 'pronoun'}
        result = cedict.isFunctionWord(word)
        self.assertTrue(result)

    def testIsFunctionWord2(self):
        word = {'traditional': u'尊者', 'grammar': 'noun'}
        result = cedict.isFunctionWord(word)
        self.assertFalse(result)

    def testIsFunctionWord3(self):
        word = {'traditional': u'有', 'grammar': 'verb'}
        result = cedict.isFunctionWord(word)
        self.assertTrue(result)

    def testPreferWord1(self):
        word1 = {'id': '1234', 'traditional': u'尊者', 'grammar': 'noun'}
        word2 = {'id': '4321', 'traditional': u'尊者', 'grammar': 'pronoun'}
        word = cedict.preferWord(word1, word2)
        self.assertEqual('4321', word['id'])

    def testPreferWord2(self):
        word1 = {'id': '1234', 'traditional': u'尊者', 'grammar': 'noun', 'topic_en': 'Buddhism'}
        word2 = {'id': '4321', 'traditional': u'尊者', 'grammar': 'pronoun'}
        word = cedict.preferWord(word1, word2)
        self.assertEqual('1234', word['id'])

    def testGetGloss1(self):
        word_entry = {}
        gloss = cedict.getGloss(word_entry)
        expected = ''
        self.assertEqual(expected, gloss)

    def testGetGloss3(self):
        word = {'id': '4321', 'traditional': u'尊者', 'grammar': 'pronoun'}
        gloss = cedict.getGloss(word)
        expected = ''
        self.assertEqual(expected, gloss)

    def testGetGloss3(self):
        word = {'english': 'hello / hi / good day'}
        gloss = cedict.getGloss(word)
        expected = 'hello'
        self.assertEqual(expected, gloss)


if __name__ == '__main__':
    unittest.main()
