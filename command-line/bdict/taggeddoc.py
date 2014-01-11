"""Module to load and analyze documents in POS tagged format. =================

The tagged docs are loaded into a sequence of tagged words and the frequency
distribitions of word senses compiled.
"""

import codecs

from bdict import bigram
from bdict import unigram


class TaggedDocumentAnalyzer:
    """Class analyzes the PoS tagged documents to compile statistics.

    The frequency of parts of speech and senses for words are collected
    and written to a file.
    """

    def __init__(self):
        """Constructor for TaggedDocumentAnalyzer
        """
        self.unigram_tagger = unigram.UnigramTagger()
        self.bigram_tagger = bigram.BigramTagger()

    def WordSenseForCorpus(self):
        """Finds the word sense frequency for the entire tagged corpus.

        Return:
          A taggeddocparser.AnalysisResults object, including a dictionary structure 
          with the word sense frequency.
        """
        unigram_outfile = 'unigram.txt'
        unigram_results = self.unigram_tagger.FindFreqCorpus()
        self.unigram_tagger.SaveFreq(unigram_results.wfreq, unigram_outfile)
        bigram_outfile = 'bigram.txt'
        bigram_results = self.bigram_tagger.FindFreqCorpus()
        self.bigram_tagger.SaveFreq(bigram_results.wfreq, bigram_outfile)
        return unigram_results.wcount, unigram_outfile, bigram_outfile

