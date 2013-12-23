# -*- coding: utf-8 -*-
"""Module to compile a vocabulary from a Chinese document. ==============

The analysis is output in markdown format.
"""
import codecs
import os.path
import re

from bdict import app_exceptions
from bdict import cedict
from bdict import chinesephrase
from bdict import configmanager
from bdict import ngramfinder
from bdict import phrasematcher

DEFAULT_OUTFILE = 'temp.md'


class ChineseVocabulary:
    """Compiles vocabulary from Chinese language documents.

    """

    def __init__(self):
        manager = configmanager.ConfigurationManager()
        self.config = manager.LoadConfig()

    def BuildVocabulary(self, corpus_entry, outfile=DEFAULT_OUTFILE):
        """Builds the list of known and unknown words from the input file.

        Args:
          corpus_entry: the corpus entry that contains the source file and other
                        information
          outfile: name the output file

        Raises:
          BDictException: If the input file does not exist
        """
        # print('Creating vocabulary based on a Chinese language document.')
        dictionary = cedict.ChineseEnglishDict()
        wdict = dictionary.OpenDictionary() # Word dictionary

        directory = self.config['corpus_directory']
        infile = corpus_entry['plain_text']
        fullpath = '%s/%s' % (directory, infile)
        if not os.path.isfile(fullpath):
            raise app_exceptions.BDictException('%s is not a file' % infile)

        wc = 0
        lines = 0
        known_words = {}
        new_words = {}
        finder = ngramfinder.NGramFinder(2)
        found_start = False
        start_marker = None
        if 'start' in corpus_entry:
            start_marker = corpus_entry['start']
        else:
            found_start = True
        end_marker = None
        if 'end' in corpus_entry:
            end_marker = corpus_entry['end']
        text = ''

        with codecs.open(fullpath, 'r', "utf-8") as f:
            # print('Reading input file %s ' % fullpath)
            for line in f:
                lines += 1
                if not found_start:
                    # Look for start marker
                    if line.find(start_marker) != -1:
                        found_start = True
                    else:
                        continue
                    
                if end_marker and line.find(end_marker) != -1:
                    break

                splitter = chinesephrase.ChinesePhraseSplitter(wdict)
                words = splitter.ExtractWords(line)
                wc += len(words)
                for word in words:
                    finder.AddWord(word)
                    text += word
                    if word in wdict:
                        if word not in known_words:
                            known_words[word] = 1
                        else:
                            known_words[word] += 1
                    else:
                        if word not in new_words:
                            new_words[word] = 1
                        else:
                            new_words[word] += 1

        full_outfile = '%s/%s' % (directory, outfile)
        with codecs.open(full_outfile, 'w', "utf-8") as outf:
            print('Writing output file %s ' % full_outfile)
            source_name = corpus_entry['source_name']
            source = corpus_entry['source']
            reference = corpus_entry['reference']
            outf.write('## Vocabulary for source document %s\n' % source_name)
            outf.write('Source file: %s<br/>\n' % infile)
            if 'uri' in corpus_entry:
                uri = corpus_entry['uri']
                outf.write('Document Source URL: %s<br/>\n' % uri)
            outf.write('Source: %s<br/>\n' % source)
            outf.write('Reference: %s<br/>\n' % reference)
            if 'translator' in corpus_entry:
                translator = corpus_entry['translator']
                outf.write('Translator: %s<br/>\n' % translator)
            if 'start' in corpus_entry:
                start = corpus_entry['start']
                outf.write('Start marker: %s<br/>\n' % start)
            if 'end' in corpus_entry:
                end = corpus_entry['end']
                outf.write('End marker: %s<br/>\n' % end)
            outf.write('Lines read: %d<br/>\n' % lines)
            outf.write('### Word count\n')
            num_known = len(known_words)
            num_new = len(new_words)
            outf.write('Word count: %d, unique words: %d, known words: %d, new words: %d\n' % 
                  (wc, num_known + num_new, num_known, num_new))
            outf.write('')
            self._PrintFrequencyKnown(known_words, wdict, outf, wc)
            outf.write('')
            self._PrintFrequencyNew(new_words, outf, wc, 'New Words')
            bigrams = finder.GetNGrams(2)
            self._PrintFrequencyNew(bigrams, outf, wc, 'Bigrams')
            matcher = phrasematcher.PhraseDataset()
            matcher.Load()
            phrases = matcher.Matches(text)
            self._PrintPhrases(phrases, outf, wc, 'Matching entries in phrase dataset')

    def _PrintFrequencyKnown(self, word_freq, sdict, outf, wc):
        """Prints the set of known words with markdown links.

        Split the set into functional and non-functional words.

        args:
          word_freq: A dictionary of words
          sdict: The dictionary
          outf: file object to send output to
          wc: the total word count
        """
        function_words = {}
        nonfunction_words = {}
        for k in word_freq.keys():
            word = sdict[k]
            if cedict.isFunctionWord(word):
                function_words[k] = word_freq[k]
            else:
                nonfunction_words[k] = word_freq[k]
        outf.write('### Frequency of non-function words:\n')
        outf.write('Word, frequency, relative frequency per 1000 words\n\n')
        for k in sorted(nonfunction_words, key=lambda key: -nonfunction_words[key]):
            self._PrintKnownWord(k, word_freq[k], sdict, outf, wc)
        outf.write('### Frequency of function words:\n')
        outf.write('Word, frequency, relative frequency per 1000 words\n\n')
        for k in sorted(function_words, key=lambda key: -function_words[key]):
            self._PrintKnownWord(k, word_freq[k], sdict, outf, wc)

    def _PrintFrequencyNew(self, word_freq, outf, wc, title):
        """Prints the set of words without links.

        Since the words are not known there are no links to the dictionary.

        args:
          word_freq: A dictionary of words
          outf: file object to send output to
          wc: the total word count
        """
        outf.write('### Frequency of %s\n' % title)
        if not word_freq:
            outf.write('None<br/>\n')
        else:
            for k in sorted(word_freq, key=lambda key: -word_freq[key]):
                outf.write("%s, %d<br/>\n" % (k, word_freq[k]))

    def _PrintKnownWord(self, traditional, freq, sdict, outf, wc):
        """Prints the known words with a markdown link.

        Prints the word with frequency and relative frequency.

        args:
          traditional: The traditional text of the word to print
          freq: The absolute frequency of the word
          sdict: The dictionary
          outf: file object to send output to
          wc: the total word count
        """
        word = sdict[traditional]
        word_id = word['id']
        english = word['english']
        rel_freq = 1000 * freq / float(wc)
        outf.write('[%s](word_detail.php?id=%s "%s %s"), %d, %.2f<br/>\n'
                   '' % (traditional, word_id, english, traditional, freq, rel_freq))

    def _PrintPhrases(self, phrases, outf, wc, title):
        """Prints out the set of phrase entries.

        Prints the phrase with pos tags out.

        args:
          phrases: A list of phrase entries
        """
        outf.write('### Phrase matches\n')
        if not phrases:
            outf.write('None<br/>\n')
        else:
            outf.write('Phrase, Part-of-Speech Tagged Phrase, Source\n\n')
            for phrase in phrases:
                chinese_phrase = phrase['chinese_phrase']
                pos_tagged = phrase['pos_tagged']
                pos_tagged = re.sub("<", "&lt;", pos_tagged)
                pos_tagged = re.sub(">", "&gt;", pos_tagged)
                source_name = phrase['source_name']
                outf.write("%s, %s, %s<br/>\n" % (chinese_phrase, pos_tagged, source_name))

