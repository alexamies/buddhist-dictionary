"""Module to do part-of-speech tagging. =======================================

The part-of-speech (POS) is given in Penn Chinese Treebank format. At present,
the POS is returned based on dictionary lookup. 
"""

import re

class POSTagger:
    """Class for POS tagging.
   """

    def __init__(self):
        """Constructor for POSTagger class.
        """
        dict_2_pen = {  # Dictionary for lookup of POS tag based on word entry grammar.
                      
                      'noun': 'NN',
                      'adjective': 'VA',
                      'proper noun': 'NR',
                      'verb': 'VV',
                      'adverb': 'AD',
                      'particle': '',
                      'pronoun': 'PN',
                      'numeral': 'CD',
                      'ordinal': 'OD',
                      'preposition': 'P',
                      'measure word': 'M',
                      'conjunction': 'CC',
                      'interrogative pronoun': 'PN',
                      'auxiliary verb': 'VV',
                      'idiom': 'UNKOWN',
                      'phrase': 'UNKOWN',
                      'quantity': 'UNKOWN',
                      'onomatopoeia': 'ON',
                      'phonetic': 'ON',
                      'suffix': 'UNKOWN',
                      'prefix': 'UNKOWN',
                      'radical': 'UNKOWN',
                      'interjection': 'IJ',
                      'pattern': 'UNKOWN',
                      'set phrase': 'UNKOWN',
                      'expression': 'UNKOWN',
                      'number': 'CD',
                      'foreign': 'FW'
                     }
        self.dict_2_pen = dict_2_pen

    def GetTag(self, word_entry):
        """Given the word entry, find the POS tag.

        Args:
          word_entry: the entry from the word dictionary

        Returns:
          A string representing the POS tag
        """
        if 'grammar' in word_entry:
            grammar = word_entry['grammar']
            if grammar in self.dict_2_pen:
                return self.dict_2_pen[grammar]
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

