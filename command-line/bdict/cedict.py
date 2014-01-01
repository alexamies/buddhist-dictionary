# -*- coding: utf-8 -*-
"""Module to load the Chinese to English dictionary. =========================

The dictionary is loaded into a dict structure
"""
import codecs

DICT_FILE_NAME = '../data/dictionary/words.txt'


class ChineseEnglishDict:
    """loads the Chinese to English dictionary.

    """

    def OpenDictionary(self):
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
                        entry['traditional'] = traditional
                    if traditional not in wdict:
                        entry['other_entries'] = []
                        wdict[traditional] = entry
                    else:
                        wdict[traditional]['other_entries'].append(entry)
        return wdict

def isFunctionWord(entry):
    """Determines whether the given word is a function word.

    A function word is selected based on being one of a pronoun, particle, etc.
    A special case is the word '有'.
    """
    grammar = entry['grammar']
    traditional = entry['traditional']
    if traditional == u'有':
        return True
    return grammar in ['particle', 'preposition', 'conjunction', 'adverb', 
                       'pronoun', 'interrogative pronoun', 'auxiliary verb', 
                       'phonetic', 'suffix', 'prefix', 'interjection']

def preferWord(entry1, entry2):
    """Determines which of the two terms are preferred

    Given that the two words are composed of the same characters
    prefered words are (1) Buddhist terms, (2) classical Chinese terms, 
    (3) function words. Other things being equal return the number with the
    lowest id
    """
    topic_en1 = None
    if 'topic_en' in entry1:
        topic_en1 = entry1['topic_en']
    topic_en2 = None
    if 'topic_en' in entry2:
        topic_en2 = entry2['topic_en']
    if topic_en1 == 'Buddhism':
        return entry1
    if topic_en2 ==  'Buddhism':
        return entry2
    if topic_en1 == 'Classical Chinese':
        return entry1
    if topic_en2 ==  'Classical Chinese':
        return entry2
    if isFunctionWord(entry1):
        return entry1
    if isFunctionWord(entry2):
        return entry2
    word_id1 = int(entry1['id'])
    word_id2 = int(entry2['id'])
    if word_id1 < word_id2:
        return entry1
    return entry2


def GetEnglishGloss(word_entry):
    """Extracts the English gloss from a word definition.

    Because some definitions are long, containing many English synonymns, and different
    shades of meaning, they can be inconvenient to display in gloss. This function
    takes the first term, up to the '/' delimiter.

    Args:
      word_entry: The entry of the word in the dictionary.

    Returns:
      The gloss as a Unicode string.
    """
    if not word_entry:
        return ''
    if not 'english' in word_entry:
        return ''
    english = word_entry['english']
    gloss = english.split('/')
    return gloss[0].strip()


def GetGloss(word_entry):
    """Extracts the English gloss from a word definition and combines with the pinyin.

    The gloss will be returned in the form pinyin | english. The English gloss will be
    simplified as in GetEnglishGloss()

    Args:
      word_entry: The entry of the word in the dictionary.

    Returns:
      The gloss as a Unicode string.
    """
    return '%s | %s' % (word_entry['pinyin'], GetEnglishGloss(word_entry))

