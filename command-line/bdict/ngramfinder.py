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
        # print('NGramFinder size: %d\n' % size)
        self.ngrams = {}
        self.words = []

    def AddWord(self, word):
        text_len = len(self.words)
        # print('AddWord word: %s, text_len: %d\n' % (word, text_len))
        for i in range(1, self.size): # length of n-gram, n = i + 1
            # print('AddWord i = %d\n' % i)
            if i <= text_len:
                key = ''
                for j in range(text_len-i, text_len):
                    # print('AddWord j = %d\n' % j)
                    key += self.words[j]
                key += word
                # print('AddWord key = %s\n' % key)
                if key in self.ngrams:
                    self.ngrams[key] += 1
                else:
                    self.ngrams[key] = 1
        self.words.append(word)

    def GetNGrams(self, min_frequency=1):
        """Get n-grams that have a minimum frequency.

        Args:
          min_frequency: Only n-grams above the minimum frequency will be returned.
        """
        min_ngrams = {}
        for k in sorted(self.ngrams, key=lambda key: -self.ngrams[key]):
            if self.ngrams[k] >= min_frequency:
                min_ngrams[k] = self.ngrams[k]
            else:
                break
        return min_ngrams

