"""Module to check the accuracy of a POS tagged sequence. =====================

The sequence will be compared to a standard and the accuracy of the match 
reported.
"""

import codecs

from bdict import app_exceptions

MAX_DIFFERENCES = 5

def TaggerAccuracy(standard, subject):
    """Compares the sequences for accuracy.

    Args:
      stardard: the sequence to compare against
      subject: the subject of the test

    Return:
      A floating point number between 0 and 1.

    Raises:
      BDictException: If the input file does not exist
    """
    if not standard or not subject:
        raise app_exceptions.BDictException('Input sequence null or empty')
    if len(standard) != len(subject):
        print('Length of standard: %d. Length of subject: %d.' % (len(standard), len(subject)))
        no_diff = 0
        for i in range(len(standard)):
            if standard[i] != subject[i]:
                print('Files differ at line %d.' % i)
                no_diff += 1
                if no_diff >= MAX_DIFFERENCES:
                    break
            else:
                no_diff = 0
        raise app_exceptions.BDictException('Sequence lengths do not match')
    no_matches = 0
    for i in range(len(standard)):
        if standard[i] == subject[i]:
            no_matches += 1
    return no_matches / float(len(standard))


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
            element_text = tokens[0]
            element = {'element_text': element_text}
            if len(tokens) > 1:
                tokens = tokens[1].split('[')
                element['tag'] = tokens[0]
            tagged_words.append(element)
    return tagged_words

