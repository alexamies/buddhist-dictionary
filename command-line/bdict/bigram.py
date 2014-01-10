"""Module to analyze and tag text based on bigram frequencies. ===============

The frequency distribitions of word senses compiled are bigram 
frequencies. There is relation between sequences of two words is captured.
"""

import codecs

from bdict import cedict

WORD_FREQ_FILE = 'biigram.txt'


class BigramTagger:
    """Class analyzes the PoS tagged documents to compile bigram statistics.

    The frequency of pairs of words are collected and written to a file.
    """

    def __init__(self):
        """Constructor for BigramTagger
        """
        dictionary = cedict.ChineseEnglishDict()
        self.wdict = dictionary.OpenDictionary() # Word dictionary

    def LoadBigramFreq(self):
        """Loads the bigram word sense frequency distribution from a file.

        The bigram frequencies are stored in a file. This method is used
        to load and parse that file.

        Returns:
          A dictionary structure indexed by traditional text for the Chinese words.
          The frequency data is given as a list on the dictionary entry.
        """
        wfreq = {}
        return wfreq

    def MostFrequentWord(self, traditional):
        """Find the most frequently used word sense based on bigram frequency.

        Given the traditional word text, find the best word based on word sense
        frequency.

        Args:
          traditional: traditional Chinese text for the word

        Returns:
          A dictionary word entry
        """
        word_entry = self.wdict[traditional]
        return word_entry

    def SaveUnigramFreq(self, wfreq, filename):
        """Saves the bigram word sense frequency distribution to a file.

        Use the FindBigramFreq() method to find the frequency
        distribution and this method to save it.

        Args:
          wfreq: a dictionary structure with the word sense frequency.
          filename: the file name to save the frequency distribution to.
        """
        pass

    def FindUnigramFreqCorpus(self):
        """Finds the unigram word sense frequency for the entire tagged corpus.

        Return:
          A dictionary structure with the word sense frequency.
        """
        wfreq = {}
        return wfreq

    def WordSenseFrequency(self, corpus_entry):
        """Finds the bigram word sense frequency from words in the corpus entry.

        Args:
          corpus_entry: including the file name of the tagged document

        Return:
          A dictionary structure with the word sense frequency.

        Raises:
          BDictException: If the input file does not exist
        """
        wfreq = {}
        return wfreq

