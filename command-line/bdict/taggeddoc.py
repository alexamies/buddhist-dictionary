"""Module to load and analyze documents in POS tagged format. =================

The tagged docs will loaded into a sequence of tagged words and frequency
distribitions of word senses compiled.
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
               'MSP': 'particle',
               'DEV': 'particle',
               'SP': 'particle',
               'AS': 'particle',
               'ETC': 'particle',
               'MSP': 'particle',
               'IJ': 'interjection',
               'ON': 'onomatopoeia',
               'PU': 'punctuation',
               'JJ': 'other modifier',
               'FW': 'foreign',
               'LB': 'bei- construction',
               'SB': 'other',
               'BA': 'ba- construction'
              }


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
            tokens = line.split('/')
            element = _ParseLine(line)
            tagged_words.append(element)
    return tagged_words


def SaveWordSenseFreq(wfreq, filename):
    """Saves the word sense frequency distribution to a file.

    Use the WordSenseFrequency() method to find the frequency
    distribution and this method to save it.

    Args:
      wfreq: a dictionary structure with the word sense frequency.
      filename: the file name to save the frequency distribution to.
    """
    dictionary = cedict.ChineseEnglishDict()
    wdict = dictionary.OpenDictionary() # Word dictionary
    with codecs.open(filename, 'w', "utf-8") as f:
        # print('Writing  to output file %s ' % filename)
        for k in sorted(wfreq, key=lambda key: -wfreq[key]['freq']):
            freq = wfreq[k]['freq']
            element_text = wfreq[k]['element_text']
            tag = wfreq[k]['tag']
            word_entry = _GetBestWordSense(wdict, wfreq[k])
            if not word_entry:
                print('Warning: could not find %s in dictionary.' % element_text)
                continue
            word_id = word_entry['id']
            f.write("%s\t%s\t%s\t%d\n" % (k, element_text, word_id, freq))


def WordSenseFrequency(filename):
    """Finds the word sense frequency from words in the POS tagged document.

    Puncution is removed from the tokens read from input file.

    Args:
      filename: the file name of the tagged document

    Return:
      A dictionary structure with the word sense frequency.
    """
    wfreq = {}
    with codecs.open(filename, 'r', "utf-8") as f:
        # print('Reading input file %s ' % filename)
        for line in f:
            line = line.strip()
            if not line:
                continue
            element = _ParseLine(line)
            if 'tag' not in element:
                print('Warning: element has no tag "%s"' % element)
                continue
            tag = element['tag'].strip()
            if tag == u'PU':
                continue
            #  print('tag is "%s"' % tag)
            if line in wfreq:
                elem = wfreq[line]
                elem['freq'] += 1
            else:
                element['freq'] = 1
                wfreq[line] = element
    return wfreq


def _GetBestWordSense(wdict, wfreq_entry):
    element_text = wfreq_entry['element_text']
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
        english = wfreq_entry['english']
        if not _GrammarMatch(tag, grammar) or not _GlossMatch(wfreq_entry, word_entry):
            # print('Tag %s for word %s grammar %s does not match grammar.' % (tag, element_text, grammar))
            if 'other_entries' not in word_entry or not word_entry['other_entries']:
                print('No other entries for word %s grammar %s gloss %s.' % (element_text, grammar, english))
            else:
                other_entries = word_entry['other_entries']
                for entry in other_entries:
                    if _GrammarMatch(tag, entry['grammar']) and _GlossMatch(wfreq_entry, entry):
                        word_entry = entry
                        break
                if not _GrammarMatch(tag, word_entry['grammar']) or not _GlossMatch(wfreq_entry, word_entry):
                    print('Could not find match for element text %s tag %s gloss "%s" among %d'
                          ' entries based on grammar or gloss.' % (element_text, tag, english, len(other_entries)+1))
    return word_entry

def _GlossMatch(wfreq_entry, wdict_entry):
    """True if the dictionary word entry english matches the word frequency gloss.
    """
    if 'english' not in wfreq_entry:
        print('No English gloss for wfreq_entry %' % wfreq_entry['element_text'])
        return False
    gloss = wfreq_entry['english']
    english = wdict_entry['english']
    return english.find(gloss) > -1

def _GrammarMatch(tag, grammar):
    """True if the dictionary word entry grammar matches the Penn POS tag
    """
    return (grammar == PENN_2_DICT[tag] 
            or
            (type(PENN_2_DICT[tag]) is list and grammar in PENN_2_DICT[tag])
           )

def _ParseLine(line):
    tokens = line.split('/')
    element_text = tokens[0]
    element = {'element_text': element_text}
    if len(tokens) > 1:
        tokens = tokens[1].split('[')
        element['tag'] = tokens[0]
        if len(tokens) > 1:
            tokens = tokens[1].split('|')
            if len(tokens) > 1:
                english = tokens[1]
                pos = english.find(u']')
                if pos > -1:
                    english = english[0:pos]
                element['english'] = english.strip()
    return element

