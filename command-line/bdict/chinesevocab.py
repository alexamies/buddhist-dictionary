# -*- coding: utf-8 -*-
"""Module to compile a vocabulary from a Chinese document. ==============

The analysis is output in markdown format.
"""
import codecs
import re

from bdict import app_exceptions
from bdict import cedict
from bdict import cjktextreader
from bdict import chinesephrase
from bdict import configmanager
from bdict import ngramfinder
from bdict import phrasematcher

DEFAULT_OUTFILE = 'temp.md'


class ChineseVocabulary:
    """Compiles vocabulary from Chinese language documents.
    """

    def __init__(self):
        """Constructor for ChineseVocabulary class.
        """
        manager = configmanager.ConfigurationManager()
        self.config = manager.LoadConfig()

    def BuildVocabulary(self, corpus_entry):
        """Builds the list of known and unknown words from the input file.

        Args:
          corpus_entry: the corpus entry that contains the source file and other
                        information

        Returns:
          The name of the file written to

        Raises:
          BDictException: If the input file does not exist
        """
        dictionary = cedict.ChineseEnglishDict()
        wdict = dictionary.OpenDictionary() # Word dictionary

        wc = 0
        known_words = {}
        new_words = {}
        finder = ngramfinder.NGramFinder(5)
        reader = cjktextreader.CJKTextReader()
        text = reader.ReadText(corpus_entry)
        splitter = chinesephrase.ChineseWordExtractor(wdict)
        words = splitter.ExtractWords(text, leave_punctuation=True)
        wc += len(words)
        for word in words:
            finder.AddWord(word)
            if not chinesephrase.isCJKPunctuation(word):
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

        infile = corpus_entry['plain_text']
        period_pos = infile.find('.')
        outfile = DEFAULT_OUTFILE
        if infile.find('.') > -1:
            outfile = '%s-analysis.md' % infile[0:period_pos]
        if self.config['analysis_directory']:
            analysis_directory = self.config['analysis_directory']
            outfile = '%s/%s' % (analysis_directory, outfile)

        with codecs.open(outfile, 'w', "utf-8") as outf:
            source_name = corpus_entry['source_name']
            source = corpus_entry['source']
            outf.write('## Vocabulary analysis for source document %s\n' % source_name)
            outf.write('Source file: %s<br/>\n' % infile)
            if 'uri' in corpus_entry:
                uri = corpus_entry['uri']
                outf.write('[Document Record] (%s "Document Record")<br/>\n' % uri)
            outf.write('Source: %s<br/>\n' % source)
            if 'reference' in corpus_entry:
                reference = corpus_entry['reference']
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
            outf.write('### Word count\n')
            num_known = len(known_words)
            num_new = len(new_words)
            outf.write('Word count: %d, unique words: %d, known words: %d, new words: %d\n' % 
                  (wc, num_known + num_new, num_known, num_new))
            outf.write('\n')
            matcher = phrasematcher.PhraseDataset()
            matcher.Load()
            phrases = matcher.Matches(text)
            self._PrintPhrases(phrases, outf, 'Matching entries in phrase dataset')
            bigrams = finder.GetNGrams(2)
            phrase_dict = matcher.Load()
            self._PrintFrequencyNew(bigrams, outf, phrase_dict, 'N-grams with frequency greater than 2')
            self._PrintFrequencyKnown(known_words, wdict, outf, wc)
            outf.write('\n')
            self._PrintFrequencyNew(new_words, outf, phrase_dict, 'New Words')
        return outfile

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
        outf.write('For words with frequency greater than 1\n\n')
        outf.write('Word, frequency, relative frequency per 1000 words\n\n')
        for k in sorted(nonfunction_words, key=lambda key: -nonfunction_words[key]):
            if 1 < word_freq[k]:
                self._PrintKnownWord(k, word_freq[k], sdict, outf, wc)
        outf.write('### Frequency of function words:\n')
        outf.write('For words with frequency greater than 1\n\n')
        outf.write('Word, frequency, relative frequency per 1000 words\n\n')
        for k in sorted(function_words, key=lambda key: -function_words[key]):
            if 1 < word_freq[k]:
                self._PrintKnownWord(k, word_freq[k], sdict, outf, wc)

    def _PrintFrequencyNew(self, word_freq, outf, phrase_dict, title):
        """Prints the set of words without links.

        Since the words are not known there are no links to the dictionary.

        args:
          word_freq: A dictionary of words
          outf: file object to send output to
          phrase_dict: the dictionary of phrases
        """
        outf.write('### Frequency of %s\n' % title)
        if not word_freq:
            outf.write('None<br/>\n')
        else:
            for k in sorted(word_freq, key=lambda key: -word_freq[key]):
                if k not in phrase_dict:
                    outf.write("%s, %d<br/>\n" % (k, word_freq[k]))
                else:
                    phrase = phrase_dict[k]
                    pid = phrase['id']
                    chinese_phrase = phrase['chinese_phrase']
                    pos_tagged = phrase['pos_tagged']
                    pos_tagged = re.sub("<", "&lt;", pos_tagged)
                    pos_tagged = re.sub(">", "&gt;", pos_tagged)
                    source_name = phrase['source_name']
                    outf.write('[%s] (phrase_detail.php?id=%s "%s"), %d\n\n' % (chinese_phrase, pid, pos_tagged, word_freq[k]))

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
        gloss = cedict.GetEnglishGloss(word)
        rel_freq = 1000 * freq / float(wc)
        outf.write('[%s](word_detail.php?id=%s "%s %s") [%s], %d, %.2f<br/>\n'
                   '' % (traditional, word_id, english, traditional, gloss, freq, rel_freq))

    def _PrintPhrase(self, phrase, outf):
        """Prints out a phrase entry.

        Prints the phrase with pos tags out.

        args:
          phrase: A list of phrase entries
        """
        pid = phrase['id']
        chinese_phrase = phrase['chinese_phrase']
        pos_tagged = phrase['pos_tagged']
        pos_tagged = re.sub("<", "&lt;", pos_tagged)
        pos_tagged = re.sub(">", "&gt;", pos_tagged)
        source_name = phrase['source_name']
        outf.write('[%s] (phrase_detail.php?id=%s "%s"), %s\n\n' % (chinese_phrase, pid, pos_tagged, source_name))

    def _PrintPhrases(self, phrases, outf, title):
        """Prints out the set of phrase entries.

        Prints the phrases with pos tags out.

        args:
          phrases: A list of phrase entries
          outf: the file to write the output to

        """
        outf.write('### %s\n\n' % title)
        if not phrases:
            outf.write('None<br/>\n')
        else:
            for phrase in phrases:
                self._PrintPhrase(phrase, outf)

