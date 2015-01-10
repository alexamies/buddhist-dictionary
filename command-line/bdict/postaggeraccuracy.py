"""Module to check the accuracy of a POS tagged sequence. =====================

The sequence will be compared to a standard and the accuracy of the match 
reported.
"""

from bdict import app_exceptions
from bdict import configmanager
from bdict import taggeddocparser

MAX_DIFFERENCES = 20


def TaggerAccuracy(corpus_entry, subject_file):
    """Compares the sequences for accuracy and prints the result.

    Args:
      corpus_entry: the corpus entry for the text
      subject_file: the subject of the test
    """
    if 'pos_tagged' not in corpus_entry:
        print('Could not compute accuracy: no standard tagged file.')
        return
    pos_tagged = corpus_entry['pos_tagged']
    manager = configmanager.ConfigurationManager()
    config = manager.LoadConfig()
    tagged_directory = config['tagged_directory']
    standard_file = '%s/%s' % (tagged_directory, pos_tagged)
    standard = taggeddocparser.LoadTaggedDoc(standard_file)
    if not standard:
        print('Standard file does not exist.')
        return
    subject = taggeddocparser.LoadTaggedDoc(subject_file)
    if not standard or not subject:
        raise app_exceptions.BDictException('Input sequence null or empty')
    if len(standard) != len(subject):
        print('Length of standard: %d. Length of subject: %d.' % (len(standard), len(subject)))
        no_diff = 0
        for i in range(len(standard)):
            if i == len(subject):
                break
            if standard[i] != subject[i]:
                print('Files differ at line %d.' % i)
                no_diff += 1
                if no_diff >= MAX_DIFFERENCES:
                    break
            else:
                no_diff = 0
        print('Sequence lengths do not match')
        return
    no_matches = 0
    for i in range(len(standard)):
        if standard[i] == subject[i]:
            no_matches += 1
    accuracy = no_matches / float(len(standard))
    print('Tagging accuracy: %f' % accuracy)

