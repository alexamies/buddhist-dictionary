# -*- coding: utf-8 -*-
"""Module to collect corpus statistics.

The corpus vocabulary analysis will be output to file STATS_FILE.
"""
import codecs

STATS_FILE = '../data/stats/corpus_stats.txt'

class CorpusStats:
    """Collects and write the corpus statistics.

    Vocabulary analysis results are added and collected.
    """

    def __init__(self):
        """Constructor for CorpusStats class.
        """
        self._results = []

    def Add(self, result):
        """Add a new vocabular analysis result 

       Args:
            A vocabular analysis result object
        """
        self._results.append(result)

    def WriteStats(self):
        """Writes vocabulary analysis results to a file.
        """
        if len(self._results) < 2:
            print("Not writing corpus statistics")
            for result in self._results:
                print("Vocabulary analysis written to file %s" % 
                      result['outfile'])
            return
        with codecs.open(STATS_FILE, 'w', "utf-8") as outf:
            outf.write('source_name\tword_count\tcharacter_count\t'
                       'unique_words\n')
            for result in self._results:
                outf.write('%s\t%s\t%s\t%s\n' % (result['source_name'], 
                           result['word_count'], result['character_count'],
                           result['unique_words']))
        print("Vocabulary analysis written for %d files" % len(self._results))
       