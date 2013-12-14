# -*- coding: utf-8 -*-
"""Command line to compile a vocabulary from a Chinese document. ==============

The analysis is output in markdown format.
"""
import regex

DICT_FILE_NAME = '../data/dictionary/sanskrit.txt'


def BuildVocabulary(directory, infile):
    """Builds the list of known and unknown words from the input file.

    Args:
      directory: the directory that contains the target file
      infile: the target file
    """
    sdict = _OpenDictionary()
    fullpath = '%s/%s' % (directory, infile)
    f = open(fullpath, 'r')
    wc = 0
    known_words = {}
    new_words = {}
    for line in f:
        if line.find('---END---') != -1:
            break
        words = line.split()
        wc += len(words)
        for token in words:
            word = _StripPunctuation(token)
            if not word:
                continue
            word = _ConvertNonStandard(word)
            if word in sdict:
                if word not in known_words:
                    known_words[word] = 1
                else:
                    known_words[word] += 1
            else:
                if word not in new_words:
                    new_words[word] = 1
                else:
                    new_words[word] += 1
    print('## Vocabulary for %s\n' % infile)
    print('### Word count\n')
    num_known = len(known_words)
    num_new = len(new_words)
    print('Word count: %d, unique words: %d, known words: %d, new words: %d' % 
          (wc, num_known + num_new, num_known, num_new))
    print('')
    print('### Frequency of known words:')
    _PrintFrequencyLinks(known_words, sdict)
    print('')
    print('### Frequency of new words')
    _PrintFrequency(new_words)


def _OpenDictionary():
    """Reads the dictionary into memory
    """
    f = open(DICT_FILE_NAME, 'r')
    sdict = {}
    for line in f:
        line = line.strip()
        if not line:
            continue
        fields = line.split('\t')
        if fields and len(fields) >= 10:
            entry = {}
            entry['id'] = fields[0]
            entry['word_id'] = fields[1]
            entry['latin'] = fields[2]
            entry['iast'] = fields[3]
            entry['dev'] = fields[4]
            entry['pali'] = fields[5]
            entry['traditional'] = fields[6]
            entry['english'] = fields[7]
            sdict[entry['iast']] = entry
    return sdict


def _PrintFrequencyLinks(word_freq, sdict):
    """Prints the set of words with markdown links

    args:
        word_freq: A dictionary of words
        sdict: The dictionary
    """
    keys = sorted(word_freq, key=lambda key: -word_freq[key])
    for k in keys:
        word = sdict[k]
        english = word['english']
        traditinal = word['traditional']
        print("[%s](sanskrit_query.php?word=%s '%s %s') : %d<br/>" % (k, k, english, traditinal, word_freq[k]))


def _PrintFrequency(word_freq):
    """Prints the set of words without links

    args:
        word_freq: A dictionary of words
    """
    keys = sorted(word_freq, key=lambda key: -word_freq[key])
    for k in keys:
        print("%s : %d<br/>" % (k, word_freq[k]))


def _StripPunctuation(token):
    """Strips punction and numbers from the token to make it a word.

    args:
        token: A string token
    """
    return regex.sub('[\|\-\(\)\?\,0-9]', '', token)


def _ConvertNonStandard(token):
    """Strips punction and numbers from the token to make it a word.

    args:
        token: A string token
    """
    return regex.sub('ṁ', 'ṃ', token)

