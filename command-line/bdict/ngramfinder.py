"""Module to find frequency of n-grams. ========================================

This module should be created and used to accumulated a collection of n-grams 
when scanning a stream of text.
"""


class NGramFinder:
    """Finds n-grams of a given size. Only bigrams supported at the moment.

    Stores the n-grams is a dict structure. They keys are the n words concatenated
    together.
    """

    def __init__(self, size=2):
        """Constructor for class.

        Args:
          size: the length of n-gram to. Should be an integer >= 2.
        """
        self.size = size
        self.ngrams = {}
        self.words = []

    def AddWord(self, word):
        text_len = len(self.words)
        if text_len > 0:
            key = self.words[text_len-1] + word
            if key in self.ngrams:
                self.ngrams[key] += 1
            else:
                self.ngrams[key] = 1
        self.words.append(word)

    def GetNGrams(self, min_frequency=1):
        """Get n-grams that have a minimum frequency.

        Args:
          min_frequency: Only n-grams above the minimum will be returned.
        """
        min_ngrams = {}
        for k in sorted(self.ngrams, key=lambda key: -self.ngrams[key]):
            if self.ngrams[k] >= min_frequency:
                min_ngrams[k] = self.ngrams[k]
            else:
                break
        return min_ngrams

