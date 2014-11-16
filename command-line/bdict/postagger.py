"""Module to do part-of-speech tagging. =======================================

The part-of-speech (POS) is given in Penn Chinese Treebank format. At present,
the POS is returned based on dictionary lookup. 
"""
import codecs
import re

from bdict import bigram
from bdict import cedict
from bdict import unigram

TAG_DEF_FILE = '../data/dictionary/pos_penn.txt'

DICT_2_PENN = {  # Dictionary for lookup of POS tag based on word entry grammar.
               'noun': 'NN',
               'adjective': 'VA',
               'proper noun': 'NR',
               'verb': 'VV',
               'adverb': 'AD',
               'particle': 'MSP',
               'pronoun': 'PN',
               'numeral': 'CD',
               'ordinal': 'OD',
               'preposition': 'P',
               'measure word': 'M',
               'conjunction': 'CC',
               'interrogative pronoun': 'PN',
               'auxiliary verb': 'VV',
               'idiom': 'PHRASE',
               'phrase': 'PHRASE',
               'quantity': 'CD',
               'onomatopoeia': 'ON',
               'phonetic': 'ON',
               'suffix': 'MSP',
               'prefix': 'MSP',
               'radical': 'RADICAL',
               'interjection': 'IJ',
               'pattern': 'PATTERN',
               'set phrase': 'NR',
               'expression': 'PHRASE',
               'number': 'CD',
               'foreign': 'FW'
              }


class POSTagger:
    """Class for POS tagging.
   """

    def __init__(self, charset='Traditional'):
        """Constructor for POSTagger class.

        Args:
          charset: The character set that the source document is written
                   in, either 'Traditional' (default) or 'Simplified'
        """
        self.tag_defs = self._LoadTagDefs()
        self.unigram_tagger = unigram.UnigramTagger(charset=charset)
        self.bigram_tagger = bigram.BigramTagger(charset=charset)
        dictionary = cedict.ChineseEnglishDict()
        self.wdict = dictionary.OpenDictionary(charset=charset) # Word dictionary

    def GetTag(self, word_entry):
        """Given the word entry, find the POS tag.

        Args:
          word_entry: the entry from the word dictionary

        Returns:
          A string representing the POS tag
        """
        for tag_def in self.tag_defs:
            if 'words' in tag_def:
                if word_entry['traditional'] in tag_def['words']:
                    return tag_def['tag']
        if 'grammar' in word_entry:
            grammar = word_entry['grammar']
            if grammar in DICT_2_PENN:
                return DICT_2_PENN[grammar]
        return 'UNKOWN'

    def GetTaggedWords(self, phrase_entry):
        """Given the word entry, find the POS tag.

        Args:
          phrase_entry: the entry from the phrase memory dataset

        Returns:
          A list of tagged words
        """
        tagged_words = []
        if 'pos_tagged' in phrase_entry:
            pos_tagged = phrase_entry['pos_tagged']
            matches = re.split('] ', pos_tagged, re.UNICODE)
            if matches:
               for match in matches:
                   if match[0] != '<':
                       tagged_words.append(match + ']')
        elif 'chinese_phrase' in phrase_entry:
            chinese_phrase = phrase_entry['chinese_phrase']
            tagged_word = '%s/%s' % (chinese_phrase, 'PHRASE')
            tagged_words.append(tagged_word)
        return tagged_words

    def MostFrequentWord(self, word, previous=None):
        """Find the most frequently used word sense.

        Given the traditional word text, find the best word based on word sense
        frequency.

        Args:
          word: the Chinese text for the word

        Returns:
          A dictionary word entry
        """
        word = None
        # print('MostFrequentWord traditional = %s, previous = %s' % (traditional, previous))
        if previous:
            word = self.bigram_tagger.MostFrequentWord(previous, word)
        if not word:
            word = self.unigram_tagger.MostFrequentWord(word)
        return word

    def TagWord(self, word, previous=None):
        """Find the most frequently used word sense and tag it.

        Given the traditional word text, find the best word based on word sense
        frequency and create the tag for the word.

        Args:
          word: the Chinese text for the word

        Returns:
          A string representing the POS tag
        """
        if word not in self.wdict:
            return '%s/%s[%s | %s]' % (word, 'UNKNOWN', 'PINYIN', 'ENGLISH')
        word_entry = self.MostFrequentWord(word)
        tag = self.GetTag(word_entry)
        pinyin = word_entry['pinyin']
        gloss = cedict.GetGloss(word_entry)
        return '%s/%s[%s]' % (word, tag, gloss)

    def _LoadTagDefs(self):
        """Reads the POS tag definitions into memory.

        Puts the words for the closed sets into set structures.
        """
        tag_defs = []
        with codecs.open(TAG_DEF_FILE, 'r', "utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                fields = line.split('\t')
                if fields and len(fields) >= 3:
                    tag_def = {}
                    tag_def['tag'] = fields[0]
                    tag_def['name'] = fields[1]
                    if fields[2] != '\\N':
                        tag_def['words'] = set(fields[2].split())
                    tag_defs.append(tag_def)
        return tag_defs

