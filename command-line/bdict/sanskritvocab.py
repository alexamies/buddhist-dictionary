# -*- coding: utf-8 -*-
"""Module to compile a vocabulary from a Sanskrit document. =============

The analysis is output in markdown format.
"""
import codecs
import regex

from bdict import configmanager

DICT_FILE_NAME = '../data/dictionary/sanskrit.txt'
COMPOUNDS_FILE_NAME = '../data/dictionary/sanskrit_compounds.txt'
DEFAULT_OUTFILE_HTML = 'diamond-sutra-sanskrit-analysis.html'


class SanskritVocabulary:
    """Compiles vocabulary from Sanskrit language documents.

    """

    def __init__(self):
        manager = configmanager.ConfigurationManager()
        self.config = manager.LoadConfig()

    def BuildVocabulary(self, corpus_entry):
        """Builds the list of known and unknown words from the input file.

        Args:
          corpus_entry: the corpus entry that contains the source file and other
                        information
        """
        sdict = self.OpenDictionary()
        cdict = self.OpenCompoundsList()
        combined_dict = dict(sdict.items() + cdict.items())
        directory = self.config['corpus_directory']
        infile = corpus_entry['plain_text']
        fullpath = '%s/%s' % (directory, infile)
        with codecs.open(fullpath, 'r', "utf-8") as f:
            wc = 0
            known_words = {}
            new_words = {}
            for line in f:
                if line.find('---END---') != -1:
                    break
                words = line.split()
                wc += len(words)
                for token in words:
                    word = StripPunctuation(token)
                    if not word:
                        continue
                    word = ConvertNonStandard(word)
                    if word in combined_dict:
                        if word not in known_words:
                            known_words[word] = 1
                        else:
                            known_words[word] += 1
                    else:
                        if word not in new_words:
                            new_words[word] = 1
                        else:
                            new_words[word] += 1
        outfile = DEFAULT_OUTFILE_HTML
        with codecs.open(outfile, 'w', "utf-8") as outf:
            outf.write('<h2>Vocabulary for %s [experimental]</h2>' % infile)
            outf.write('<h3>Word count</h3>')
            num_known = len(known_words)
            num_new = len(new_words)
            outf.write('<p>Word count: %d, unique words: %d, known words: %d, new words: %d</p>' % 
                  (wc, num_known + num_new, num_known, num_new))
            outf.write('<h3>Frequency of known words</h3>')
            self._PrintFrequencyLinks(outf, known_words, combined_dict)
            outf.write('\n')
            outf.write('<h3>Frequency of new words</h3>')
            self._PrintFrequency(outf, new_words)
        print('Output written to %s' % outfile)

    def OpenDictionary(self):
        """Reads the dictionary into memory
        """
        with codecs.open(DICT_FILE_NAME, 'r', "utf-8") as f:
            sdict = {}
            for line in f:
                line = line.strip()
                if not line:
                    continue
                fields = line.split('\t')
                if fields and len(fields) >= 11:
                    entry = {}
                    entry['id'] = fields[0]
                    entry['word_id'] = fields[1]
                    entry['latin'] = fields[2]
                    entry['iast'] = fields[3]
                    entry['dev'] = fields[4]
                    if fields[5] != '\N':
                        entry['pali'] = fields[5]
                    entry['traditional'] = fields[6]
                    entry['english'] = fields[7]
                    if fields[8] != '\N':
                        entry['notes'] = fields[8]
                    entry['grammar'] = fields[9]
                    if fields[10] != '\N':
                        entry['stem'] = fields[10]
                    sdict[entry['iast']] = entry
        return sdict

    def OpenCompoundsList(self):
        """Reads the dictionary into memory
        """
        with codecs.open(COMPOUNDS_FILE_NAME, 'r', "utf-8") as f:
            compounds_dict = {}
            for line in f:
                line = line.strip()
                if not line:
                    continue
                fields = line.split('\t')
                if fields and len(fields) >= 8:
                    entry = {}
                    entry['id'] = fields[0]
                    entry['iast'] = fields[1]
                    entry['english'] = fields[2]
                    if fields[3] != '\N':
                        entry['traditional'] = fields[3]
                    entry['no_parts'] = fields[4]
                    entry['source'] = fields[5]
                    entry['parts'] = fields[6]
                    if fields[7] != '\N':
                        entry['notes'] = fields[7]
                    compounds_dict[entry['iast']] = entry
        return compounds_dict

    def _PrintFrequencyLinks(self, outf, word_freq, combined_dict):
        """Prints the set of words with markdown links

        args:
          word_freq: A dictionary of words
          combined_dict: The combined word + compounds word dictionary
        """
        keys = sorted(word_freq, key=lambda key: -word_freq[key])
        for k in keys:
            word = combined_dict[k]
            title = "%s" % word['english']
            iast = "Word: %s<br/>" % k
            english = "English: %s<br/>" % word['english']
            stem = ""
            if 'stem' in word:
                stem = "Stem / root: %s<br/>" % word['stem']
            dev = ""
            if 'dev' in word:
                dev = "Devanagari: %s<br/>" % word['dev']
            pali = ""
            if 'pali' in word:
                pali = "Pali: %s<br/>" % word['pali']
            chinese = ''
            if 'traditional' in word:
                chinese = "Chinese: %s<br/>" % word['traditional']
            grammar = ""
            if 'grammar' in word:
                grammar = "Grammar: %s<br/>" % word['grammar']
            notes = ""
            if 'notes' in word:
                notes = "Notes: %s" % word['notes']
            parts = ""
            if 'parts' in word:
                parts = "Parts: %s<br/>" % word['parts']
            content = "%s %s %s %s %s %s %s %s %s" % (iast, english, stem, dev, pali, chinese, grammar, parts, notes)
            outf.write('<div><a href="#" class="dict-entry" data-toggle="popover"'
                       ' title="%s" data-content="%s">%s</a> %d</div>' % (title, content, k, word_freq[k]))


    def _PrintFrequency(self, outf, word_freq):
        """Prints the set of words without links

        args:
          word_freq: A dictionary of words
        """
        keys = sorted(word_freq, key=lambda key: -word_freq[key])
        for k in keys:
            outf.write("<div>%s : %d</div>" % (k, word_freq[k]))


def StripPunctuation(token):
    """Strips punction and numbers from the token to make it a word.

    args:
        token: A string token
    """
    return regex.sub('[\|\-\(\)\?\,0-9]', '', token)


def ConvertNonStandard(token):
    """Strips punction and numbers from the token to make it a word.

    args:
      token: A string token
    """
    return regex.sub('ṁ', 'ṃ', token)

