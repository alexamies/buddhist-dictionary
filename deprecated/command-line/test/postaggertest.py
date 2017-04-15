# -*- coding: utf-8 -*-
"""Unit tests for the bdict.taggeddoc module.

Tests the methods for part-of-speech tagging.
"""
import unittest

from bdict import postagger


class POSTaggerTest(unittest.TestCase):

    def testGetTag1(self):
        tagger = postagger.POSTagger()
        word_entry = {'grammar': 'noun', 'traditional': u'苦厄'}
        tag = tagger.GetTag(word_entry)
        self.assertEqual('NN', tag)

    def testGetTag2(self):
        tagger = postagger.POSTagger()
        word_entry = {'grammar': 'verb', 'traditional': u'為'}
        tag = tagger.GetTag(word_entry)
        self.assertEqual('VC', tag)

    def testGetTaggedWords1(self):
        tagger = postagger.POSTagger()
        phrase_entry = {'chinese_phrase': 'du iyqie ku e',
                        'pos_tagged': 'du/VV[du | overcome] yiqie/DT[yiqie | all] kue/NN[ku e | suffering] <overcoming all suffering>'
                       }
        tagged_words = tagger.GetTaggedWords(phrase_entry)
        self.assertTrue(tagged_words)
        # for word in tagged_words:
            # print(word)
        self.assertEqual(3, len(tagged_words))

    def testGetTaggedWords2(self):
        tagger = postagger.POSTagger()
        phrase_entry = {'chinese_phrase': u'度一切苦厄',
                        'pos_tagged': u'度/VV[dù | overcome] 一切/DT[yīqiè | all] 苦厄/NN[kŭ è | suffering] <overcoming all suffering>'
                       }
        tagged_words = tagger.GetTaggedWords(phrase_entry)
        self.assertTrue(tagged_words)
        # for word in tagged_words:
            # print(word)
        self.assertEqual(3, len(tagged_words))
        self.assertEqual(u'度/VV[dù | overcome]', tagged_words[0])

    def testLoadTagDefs(self):
        tagger = postagger.POSTagger()
        tag_defs = tagger._LoadTagDefs()
        self.assertTrue(tag_defs)
        self.assertEqual(31, len(tag_defs))
        for tag_def in tag_defs:
            if tag_def['tag'] == u'VC':
                self.assertTrue('words' in tag_def)
                self.assertTrue(u'為' in tag_def['words'])
            if tag_def['tag'] == u'VE':
                self.assertTrue('words' in tag_def)
                self.assertTrue(u'無' in tag_def['words'])
            if tag_def['tag'] == u'LC':
                self.assertTrue('words' in tag_def)
                self.assertTrue(u'北' in tag_def['words'])
            if tag_def['tag'] == u'DT':
                self.assertTrue('words' in tag_def)
                self.assertTrue(u'各' in tag_def['words'])
            if tag_def['tag'] == u'CC':
                self.assertTrue('words' in tag_def)
                self.assertTrue(u'與' in tag_def['words'])

    def testTagWord1(self):
        tagger = postagger.POSTagger()
        traditional = u'hello'
        tagged_word = tagger.TagWord(traditional)
        expected = u'hello/UNKNOWN[PINYIN | ENGLISH]'
        self.assertEqual(expected, tagged_word)

    def testTagWord2(self):
        tagger = postagger.POSTagger()
        traditional = u'為'
        tagged_word = tagger.TagWord(traditional)
        expected = u'為/VC[wèi | for]'
        self.assertEqual(expected, tagged_word)

    def testTagWord3(self):
        tagger = postagger.POSTagger()
        traditional = u'是'
        tagged_word = tagger.TagWord(traditional)
        expected = u'是/VC[shì | this]'
        self.assertEqual(expected, tagged_word)

    def testMostFrequentWord1(self):
        tagger = postagger.POSTagger()
        traditional = u'是'
        word = tagger.MostFrequentWord(traditional)
        expected = u'17908'
        self.assertEqual(expected, word['id'])

    def testMostFrequentWord2(self):
        tagger = postagger.POSTagger()
        traditional = u'故'
        previous = u'以'
        word = tagger.MostFrequentWord(traditional, previous=previous)
        expected = u'7115'
        self.assertEqual(expected, word['id'])

    def testMostFrequentWord3(self):
        tagger = postagger.POSTagger()
        traditional = u'也'
        word = tagger.MostFrequentWord(traditional)
        expected = u'8853'
        self.assertEqual(expected, word['id'])


if __name__ == '__main__':
    unittest.main()

