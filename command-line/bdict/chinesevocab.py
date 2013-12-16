# -*- coding: utf-8 -*-
"""Module to compile a vocabulary from a Chinese document. ==============

The analysis is output in markdown format.
"""
import codecs
import os.path

from bdict import app_exceptions
from bdict import chinesephrase

DICT_FILE_NAME = '../data/dictionary/words.txt'
DEFAULT_OUTFILE = 'temp.md'


class ChineseVocabulary:
    """Compiles vocabulary from Chinese language documents.

    """

    def BuildVocabulary(self, directory, infile, outfile=DEFAULT_OUTFILE):
        """Builds the list of known and unknown words from the input file.

        Args:
          directory: the directory that contains the target file
          infile: name the target file
          outfile: name the output file

        Raises:
          BDictException: If the input file does not exist
        """
        # print('Creating vocabulary based on a Chinese language document.')
        wdict = self._OpenDictionary() # Word dictionary

        fullpath = '%s/%s' % (directory, infile)
        if not os.path.isfile(fullpath):
            raise app_exceptions.BDictException('%s is not a file' % infile)

        wc = 0
        lines = 0
        known_words = {}
        new_words = {}
        with codecs.open(fullpath, 'r', "utf-8") as f:
            print('Reading input file %s ' % fullpath)
            for line in f:
                lines += 1
                if line.find('---END---') != -1:
                    break
                splitter = chinesephrase.ChinesePhraseSplitter(wdict)
                words = splitter.ExtractWords(line)
                wc += len(words)
                for word in words:
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
            outf.write('## Vocabulary for %s\n' % infile)
            outf.write('Lines read: %d<br/>\n' % lines)
            outf.write('### Word count\n')
            num_known = len(known_words)
            num_new = len(new_words)
            outf.write('Word count: %d, unique words: %d, known words: %d, new words: %d\n' % 
                  (wc, num_known + num_new, num_known, num_new))
            outf.write('')
            outf.write('### Frequency of known words:\n')
            self._PrintFrequencyLinks(known_words, wdict, outf)
            outf.write('')
            outf.write('### Frequency of new words\n')
            self._PrintFrequency(new_words, outf)

    def _OpenDictionary(self):
        """Reads the dictionary into memory
        """
        wdict = {}
        with codecs.open(DICT_FILE_NAME, 'r', "utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                fields = line.split('\t')
                if fields and len(fields) >= 10:
                    entry = {}
                    entry['id'] = fields[0]
                    entry['simplified'] = fields[1]
                    entry['traditional'] = fields[2]
                    entry['pinyin'] = fields[3]
                    entry['english'] = fields[4]
                    entry['grammar'] = fields[5]
                    traditional = entry['traditional']
                    if traditional == '\\N':
                        traditional = entry['simplified']
                    wdict[traditional] = entry
        return wdict

    def _PrintFrequencyLinks(self, word_freq, sdict, outf):
        """Prints the set of words with markdown links

        args:
          word_freq: A dictionary of words
          sdict: The dictionary
          outf: file object to send output to
        """
        keys = sorted(word_freq, key=lambda key: -word_freq[key])
        for k in keys:
            word = sdict[k]
            english = word['english']
            traditinal = word['traditional']
            outf.write("[%s](sanskrit_query.php?word=%s '%s %s') : %d<br/>\n" % (k, k, english, traditinal, word_freq[k]))

    def _PrintFrequency(self, word_freq, outf):
        """Prints the set of words without links

        args:
          word_freq: A dictionary of words
          outf: file object to send output to
        """
        keys = sorted(word_freq, key=lambda key: -word_freq[key])
        for k in keys:
            outf.write("%s : %d<br/>\n" % (k, word_freq[k]))

