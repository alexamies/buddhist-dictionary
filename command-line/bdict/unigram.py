"""Module to analyze and tag text based on unigram frequencies. ===============

The frequency distribitions of word senses compiled are simple unigram 
frequencies. There is no relation between sequences of words captured.
"""

import codecs

from bdict import app_exceptions
from bdict import cedict
from bdict import configmanager
from bdict import corpusmanager
from bdict import taggeddocparser

WORD_FREQ_FILE = 'unigram.txt'


class UnigramTagger:
    """Class analyzes the PoS tagged documents to compile statistics.

    The frequency of parts of speech and senses for words are collected
    and written to a file.
    """

    def __init__(self):
        """Constructor for UnigramTagger
        """
        dictionary = cedict.ChineseEnglishDict()
        self.wdict = dictionary.OpenDictionary() # Word dictionary
        self.wfreq = self.LoadUnigramFreq() # unigram word sense frequencies
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

    def LoadUnigramFreq(self):
        """Loads the unigram word sense frequency distribution from a file.

        The unigram frequencies are stored in a file. This method is used
        to load and parse that file.

        Returns:
          A dictionary structure indexed by traditional text for the Chinese word.
          The frequency data is given as a list on the dictionary entry.
        """
        manager = configmanager.ConfigurationManager()
        config = manager.LoadConfig()
        directory = config['data_directory']
        filename = '%s/%s' % (directory, WORD_FREQ_FILE)
        wfreq = {}
        with codecs.open(filename, 'r', "utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                tokens = line.split('\t')
                entry = {'pos_tagged_text': tokens[0].strip()}
                if len(tokens) == 4:
                    element_text = tokens[1].strip()
                    entry['element_text'] = element_text
                    entry['word_id'] = tokens[2].strip()
                    entry['frequency'] = int(tokens[3])
                    if element_text not in wfreq:
                        wfreq[element_text] = [entry]
                    else:
                        wfreq[element_text].append(entry)
                else:
                    print('Did not get expected number of tokens for line: %s' % line)
        return wfreq

    def MostFrequentWord(self, traditional):
        """Find the most frequently used word sense based on unigram frequency.

        Given the traditional word text, find the best word based on word sense
        frequency.

        Args:
          traditional: traditional Chinese text for the word

        Returns:
          A dictionary word entry
        """
        word_entry = self.wdict[traditional]
        if (traditional in self.wfreq):
            # Most frequently occuring is at the head of the list
            wf_entry = self.wfreq[traditional][0]
            word_id = wf_entry['word_id']
            # print('%s looking for word id %s' % (traditional, word_id))
            if word_id != word_entry['id']:
                for w_entry in word_entry['other_entries']:
                    # print('%s found id %s' % (traditional, w_entry['id']))
                    if word_id == w_entry['id']:
                        word_entry = w_entry
                        break
        return word_entry

    def SaveFreq(self, wfreq, filename):
        """Saves the unigram word sense frequency distribution to a file.

        Use the FindUnigramFreq() method to find the frequency
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
                element_text = wfreq[k]['element_text']
                f.write("%s\t%s\t%s\t%d\n" % (tagged_text, element_text, k, freq))

    def WordSenseFrequency(self, corpus_entry):
        """Finds the unigram word sense frequency from words in the corpus entry.

        The corpus entry should include a POS tagged document. Otherwise,
        an exception will be generated. Puncution is removed from the
        tokens read from input file. The key is the word id from the
        words table.

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
        for element in tagged_words:
            if 'tag' not in element:
                print('Warning: element has no tag "%s"' % element)
                continue
            tag = element['tag']
            if tag == u'PU':
                continue
            self.wcount += 1
            word_entry = taggeddocparser.GetBestWordSense(self.wdict, element)
            element_text = element['element_text']
            # tagged_text = element['tagged_text']
            # print('WordSenseFrequency tag "%s", element_text "%s" tagged_text "%s"' % (tag, element_text, tagged_text))
            if not word_entry:
                print('WordSenseFrequency warning: could not find %s in dictionary.' % element_text)
                continue
            word_id = word_entry['id']
            if word_id in wfreq:
                elem = wfreq[word_id]
                elem['freq'] += 1
            else:
                element['freq'] = 1
                wfreq[word_id] = element
        return wfreq

