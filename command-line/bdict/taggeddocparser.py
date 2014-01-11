"""Module to parse documents in POS tagged format. ============================

These methods are used by different POS tagging modules
"""
import codecs

from bdict import cedict

PENN_2_DICT = {  # Dictionary for lookup of word entry grammar based on POS tag.
               'VA': 'adjective',
               'VC': 'verb',
               'VE': 'verb',
               'VV': ['verb', 'auxiliary verb'],
               'NR': 'proper noun',
               'NT': 'noun',
               'NN': 'noun',
               'LC': 'preposition',
               'PN': 'pronoun',
               'DT': 'pronoun',
               'CD': 'number',
               'OD': 'ordinal',
               'M': 'measure word',
               'AD': 'adverb',
               'P': 'preposition',
               'CC': 'conjunction',
               'CS': 'conjunction',
               'DEC': 'particle',
               'DEG': 'particle',
               'MSP': ['particle', 'suffix'],
               'DEV': 'particle',
               'SP': 'particle',
               'AS': 'particle',
               'ETC': 'particle',
               'IJ': 'interjection',
               'ON': 'onomatopoeia',
               'PU': 'punctuation',
               'JJ': 'other modifier',
               'FW': 'foreign',
               'LB': 'bei- construction',
               'SB': 'other',
               'BA': 'ba- construction'
              }


class AnalysisResults:
    """Class statistics compile from PoS tagged document analysis.
    """

    def __init__(self, wfreq, wcount=0):
        """Constructor for AnalysisResults

        Args:
          wfreq: a dictionary structure with the word sense frequency
          wcount: the word count
        """
        self.wfreq = wfreq
        self.wcount = wcount


def LoadTaggedDoc(filename):
    """Loads the POS tagged document.

    Args:
      filename: the file name of the tagged document

    Return:
      The sequence of tagged words
    """
    tagged_words = []
    with codecs.open(filename, 'r', "utf-8") as f:
        # print('Reading input file %s ' % filename)
        for line in f:
            if not line.strip():
                continue
            element = ParseLine(line)
            tagged_words.append(element)
    return tagged_words


def ParseLine(line):
    line = line.strip()
    element = {'tagged_text': line}
    tokens = line.split('/')
    element_text = tokens[0].strip()
    element['element_text'] = element_text
    if len(tokens) > 1:
        tokens = tokens[1].split('[')
        element['tag'] = tokens[0].strip()
        if len(tokens) > 1:
            tokens = tokens[1].split('|')
            if len(tokens) > 1:
                english = tokens[1].strip()
                pos = english.find(u']')
                if pos > -1:
                    english = english[0:pos]
                element['english'] = english.strip()
    return element


def GetBestWordSense(wdict, wfreq_entry):
    """Gets the best sense of a word based on dictionary lookup and unigram frequency
    """
    element_text = wfreq_entry['element_text']
    tag = wfreq_entry['tag']
    if element_text not in wdict:
        print('Warning: could not find %s in dictionary.' % element_text)
        return None
    word_entry = wdict[element_text]
    if tag not in PENN_2_DICT:
        print('Warning: could not find tag %s in mapping for word %s.' % (tag, element_text))
    else:
        # find best match based on grammar
        grammar = word_entry['grammar']
        if 'english' not in wfreq_entry:
            print('No English text for entry %s' % wfreq_entry['tagged_text'])
            return word_entry
        english = wfreq_entry['english']
        if not GrammarMatch(tag, grammar) or not GlossMatch(wfreq_entry, word_entry):
            # print('Tag %s for word %s grammar %s does not match grammar.' % (tag, element_text, grammar))
            if 'other_entries' not in word_entry or not word_entry['other_entries']:
                print('No other entries for word %s grammar %s gloss %s.' % (element_text, grammar, english))
            else:
                other_entries = word_entry['other_entries']
                for entry in other_entries:
                    if GrammarMatch(tag, entry['grammar']) and GlossMatch(wfreq_entry, entry):
                        word_entry = entry
                        break
                if not GrammarMatch(tag, word_entry['grammar']) or not GlossMatch(wfreq_entry, word_entry):
                    print('GetBestWordSense: Could not find match for element '
                          'text %s tag %s gloss "%s" among %d entries based on '
                          'grammar or gloss.' % (element_text, tag, english, 
                          len(other_entries)+1))
    return word_entry


def GlossMatch(wfreq_entry, wdict_entry):
    """True if the dictionary word entry english matches the word frequency gloss.
    """
    if 'english' not in wfreq_entry:
        print('No English gloss for wfreq_entry %' % wfreq_entry['element_text'])
        return False
    gloss = wfreq_entry['english']
    english = wdict_entry['english']
    return english.find(gloss) > -1

def GrammarMatch(tag, grammar):
    """True if the dictionary word entry grammar matches the Penn POS tag
    """
    return (grammar == PENN_2_DICT[tag] 
            or
            (type(PENN_2_DICT[tag]) is list and grammar in PENN_2_DICT[tag])
           )

