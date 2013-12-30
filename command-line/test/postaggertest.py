# -*- coding: utf-8 -*-
"""Unit tests for the bdict.glossgenerator module.

Tests the methods for part-of-speech tagging.
"""
import unittest

from bdict import postagger


class POSTaggerTest(unittest.TestCase):

    def testGetTag1(self):
        tagger = postagger.POSTagger()
        word_entry = {'grammar': 'noun'}
        tag = tagger.GetTag(word_entry)
        self.assertEqual('NN', tag)

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


if __name__ == '__main__':
    unittest.main()

