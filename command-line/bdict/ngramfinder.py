"""Module to find frequency of n-grams. ========================================

This module should be created and used when scanning a stream of text.
"""

class NGramFinder:
    """Finds n-grams of a given size.

    Stores the n-grams is a dict structure. They keys are the n words concatenated
    together.
    """

    def __init__(self, size):
        self.size = size

    def AddWord(self, word):

