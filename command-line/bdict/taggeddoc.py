"""Module to load and analyze documents in POS tagged format. =================

The tagged docs are loaded into a sequence of tagged words and the frequency
distribitions of word senses compiled.
"""

import codecs

from bdict import app_exceptions
from bdict import cedict
from bdict import configmanager
from bdict import corpusmanager
from bdict import taggeddocparser
from bdict import unigram


class TaggedDocumentAnalyzer:
    """Class analyzes the PoS tagged documents to compile statistics.

    The frequency of parts of speech and senses for words are collected
    and written to a file.
    """

    def __init__(self):
        """Constructor for TaggedDocumentAnalyzer
        """
        self.wcount = 0
        self.unigram_tagger = unigram.UnigramTagger()

    def LoadTaggedDoc(self, filename):
        """Loads the POS tagged document.

        Args:
          filename: the file name of the tagged document

        Return:
          The sequence of tagged words
        """
        tagged_words = []
        with codecs.open(filename, 'r', "utf-8") as f:
            # print('Reading input file %s ' % filename)
            for line in f:
                if not line.strip():
                    continue
                tokens = line.split('/')
                element = taggeddocparser.ParseLine(line)
                tagged_words.append(element)
        return tagged_words

    def SaveWordSenseFreq(self, wfreq, filename):
        """Saves the word sense frequency distribution to a file.

        Use the WordSenseForCorpus() method to find the frequency
        distribution and this method to save it.

        Args:
          wfreq: a dictionary structure with the word sense frequency.
          filename: the file name to save the frequency distribution to.
        """
        self.unigram_tagger.SaveUnigramFreq(wfreq, filename)

    def WordSenseForCorpus(self):
        """Finds the word sense frequency for the entire tagged corpus.

        Return:
          A dictionary structure with the word sense frequency.
        """
        return self.unigram_tagger.FindUnigramFreqCorpus()

