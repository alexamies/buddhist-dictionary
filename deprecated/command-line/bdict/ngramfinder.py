"""Module to find frequency of n-grams. ========================================

This module should be created and used to accumulated a collection of n-grams 
when scanning a stream of text.
"""

from bdict import cedict
from bdict import chinesephrase
from bdict import postagger


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
        self._tagger = postagger.POSTagger()
        dictionary = cedict.ChineseEnglishDict()
        self._wdict = dictionary.OpenDictionary()

    def AddWord(self, word):
        text_len = len(self.words)
        # print('AddWord word: %s, text_len: %d\n' % (word, text_len))
        if not chinesephrase.isCJKPunctuation(word.strip()):
            for i in range(1, self.size): # length of n-gram, n = i + 1
                # print('AddWord i = %d\n' % i)
                if i <= text_len:
                    key = ''
                    for j in range(text_len-i, text_len):
                        # print('AddWord j = %d\n' % j)
                        key += self.words[j]
                    key += word
                    # print('AddWord key = %s\n' % key)
                    if ContainsPunctuation(key):
                        continue
                    if key in self.ngrams:
                        self.ngrams[key] += 1
                    else:
                        self.ngrams[key] = 1
        self.words.append(word)

    def GetNGrams(self, min_frequency=1):
        """Get a filtered list of n-grams that have a minimum frequency.

        Discard n-grams that have more than half function words or start or end
        in a function word. Assumption: function words are single character
        words.

        Args:
          min_frequency: Only n-grams above the minimum frequency will be
          returned.

        Return:
          An array of filtered n-grams
        """
        min_ngrams = {}
        for k in sorted(self.ngrams, key=lambda key: -self.ngrams[key]):
            if self.ngrams[k] >= min_frequency:
                # Check that it is not a substring of another n-gram of greater
                # frequency
                is_sub = False
                for l in sorted(self.ngrams, key=lambda key: -self.ngrams[key]):
                    if (k != l and l.find(k) > -1 and 
                        self.ngrams[l] >= self.ngrams[k]):
                        is_sub = True
                # Check number of function words
                num_function = 0 # Number of function words in n-gram
                i = 0
                for c in k:
                    if c in self._wdict:
                        most_freq_entry = self._tagger.MostFrequentWord(c, None)
                        # Check if the first or last character
                        if i == 0 or i == (len(k)-1):
                            if cedict.isFunctionWord(most_freq_entry):
                                num_function = len(k)
                                break
                        # Total the function words
                        if cedict.isFunctionWord(most_freq_entry):
                            num_function += 1
                    i += 1
                if num_function < len(k)/2 and not is_sub:
                    min_ngrams[k] = self.ngrams[k]
            else:
                break
        return min_ngrams

def ContainsPunctuation(word):
    """Tests whether the given word contains any punctuation.

    Args: 
      character: the character to test

    Returns:
      True or false
    """
    for c in word:
        if chinesephrase.isCJKPunctuation(c):
            return True
    return False

