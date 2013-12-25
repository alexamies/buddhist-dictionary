# -*- coding: utf-8 -*-
"""Module to extract words from a chunk of Chinese text. ======================

In this module:
  ChinesePhraseSplitter: Extracts words from a chunk of text.
"""
import unicodedata

CJK_PUNCTUATION = u'，、。：！？「」'

class ChineseWordExtractor:
    """Splits Chinese text into parts based on presence of words in the word dictionary.
    """

    def __init__(self, wdict):
        self.wdict = wdict

    def ExtractWords(self, text, leave_punctuation=False):
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
        i = 0
        length = len(text)
        # print('ExtractWords length = %d' % length)
        while i < length:
            c = text[i]
            # print('i = %d, name[i]: %s' % (i, unicodedata.name(c)))
            j = i + 1
            if isCJKLetter(c):
                # Find position of next puncutation mark
                while j < length:
                    if not isCJKLetter(text[j]):
                        break
                    j += 1
                # print('j = %d' % j)

                # Search back from next punction mark to find longest word
                j -= 1
                while j >= i :
                    if j == i:
                        # print('Adding word at j == i to list')
                        words.append(text[i])
                        break
                    # print('j = %d, name[j]: %s' % (j, unicodedata.name(text[j])))
                    possible = text[i:j+1]
                    # print('Testing if possible word of length %d is in dictionary' % len(possible))
                    if possible in self.wdict:
                        # print('Adding dictionary word length %d' % len(possible))
                        words.append(possible)
                        break
                    j -= 1
                j += 1
            elif leave_punctuation and isCJKPunctuation(c):
               words.append(c)
            i = j
        return words

def isCJKLetter(c):
    """Tests whether the given character is not punctuation, either European or CJK.

    Args: 
      character: the character to test

    Returns:
      True or false
    """
    try:
        return (unicodedata.name(c).find('CJK UNIFIED IDEOGRAPH') > -1)
    except ValueError:
        pass
    return False

def isCJKPunctuation(c):
    """Tests whether the given character is CJK punctuation.

    Args: 
      character: the character to test

    Returns:
      True or false
    """
    return (CJK_PUNCTUATION.find(c) > -1)

