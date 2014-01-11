"""Module to analyze and tag text based on bigram frequencies. ===============

The frequency distribitions of word senses compiled are bigram 
frequencies. There is relation between sequences of two words is captured.
"""

import codecs

from bdict import cedict
from bdict import configmanager
from bdict import corpusmanager
from bdict import taggeddocparser

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
        self.wcount = 0


    def FindFreqCorpus(self):
        """Finds the unigram word sense frequency for the entire tagged corpus.

        Return:
          A taggeddocparser.AnalysisResults object, including a dictionary structure 
          with the word sense frequency.
        """
        cmanager = corpusmanager.CorpusManager()
        tagged_entries = cmanager.GetAllTagged()
        wfreq = {}
        for entry in tagged_entries:
            wfreq_entry = self.WordSenseFrequency(entry)
            if not wfreq:
                wfreq =  wfreq_entry
            else:
                for key in wfreq_entry.keys():
                    if key not in wfreq:
                        wfreq[key] = wfreq_entry[key]
                    else:
                        wfreq[key]['freq'] += wfreq_entry[key]['freq']
        return taggeddocparser.AnalysisResults(wfreq, self.wcount)

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

    def SaveFreq(self, wfreq, filename):
        """Saves the bigram word sense frequency distribution to a file.

        Use the FindBigramFreq() method to find the frequency
        distribution and this method to save it.

        Args:
          wfreq: a dictionary structure with the word sense frequency.
          filename: the file name to save the frequency distribution to.
        """
        with codecs.open(filename, 'w', "utf-8") as f:
            # print('Writing  to output file %s ' % filename)
            for k in sorted(wfreq, key=lambda key: -wfreq[key]['freq']):
                tagged_text = wfreq[k]['tagged_text']
                freq = wfreq[k]['freq']
                previous = wfreq[k]['previous']
                element_text = wfreq[k]['element_text']
                f.write("%s\t%s\t%s\t%s\t%d\n" % (tagged_text, previous, element_text, k[1], freq))

    def WordSenseFrequency(self, corpus_entry):
        """Finds the bigram word sense frequency from words in the corpus entry.

        Args:
          corpus_entry: including the file name of the tagged document

        Return:
          A dictionary structure with the word sense frequency.

        Raises:
          BDictException: If the input file does not exist
        """
        if 'pos_tagged' not in corpus_entry:
            raise app_exceptions.BDictException('Cannot compute word sense '
                                                'frequency without a POS tagged doc '
                                                'in the corpus.')
        pos_tagged = corpus_entry['pos_tagged']
        manager = configmanager.ConfigurationManager()
        config = manager.LoadConfig()
        directory = config['tagged_directory']
        filename = '%s/%s' % (directory, pos_tagged)
        wfreq = {}
        tagged_words = taggeddocparser.LoadTaggedDoc(filename)
        previous = None, None # id and text of previous word seen
        for element in tagged_words:
            if 'tag' not in element:
                print('Warning: element has no tag "%s"' % element)
                previous = None, None
                continue
            tag = element['tag']
            if tag == u'PU':
                previous = None, None
                continue
            self.wcount += 1
            word_entry = taggeddocparser.GetBestWordSense(self.wdict, element)
            word_id = word_entry['id']
            element_text = element['element_text']
            if not previous[0]:
                previous = word_id, element_text
                continue
            # print('WordSenseFrequency tag "%s", element_text "%s"' % (tag, element_text))
            if not word_entry:
                print('WordSenseFrequency warning: could not find %s in dictionary.' % element_text)
                continue
            key = (previous[0], word_id)
            if key in wfreq:
                elem = wfreq[key]
                elem['freq'] += 1
            else:
                element['freq'] = 1
                element['previous'] = previous[1]
                wfreq[key] = element
            previous = word_id, element_text
        return wfreq

