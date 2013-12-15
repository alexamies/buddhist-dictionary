# -*- coding: utf-8 -*-
"""Module to extract words from a chunk of Chinese text. ======================

In this module:
  ExtractWords: Extracts words from a chunk of text.
"""
import unicodedata


class ChinesePhraseSplitter:
    """Splits a prhase into parts based on presence of words in a word dictionary.

        Not finished yet.
    """

    def __init__(self, wdict):
        self.wdict = wdict

    def ExtractWords(self, text):
        """Extracts words from a chunk of text.

        Algorithm is based on matching words in the dictionary maximizing the length
        of each word.

        Not finished yet.

        Args:
          text: the text to match
          wdict: the dictionary to use to look up the words in

        Returns:
          A list of words
        """
        words = []
        for c in text:
            words.append(c)
        return words

    def isCJKLetter(self, c):
        """Tests whether the given character is not punctuation, either European or CJK.

        Not finished yet.

        Args: 
          character: the character to test

        Returns:
          True or false
        """
        print('cat: %s : name: %s' % (unicodedata.category(c), unicodedata.name(c)))
        return c in self.wdict

