"""Module to check the accuracy of a POS tagged sequence. =====================

The sequence will be compared to a standard and the accuracy of the match 
reported.
"""

from bdict import app_exceptions

MAX_DIFFERENCES = 20


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
            if i == len(subject):
                break
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

