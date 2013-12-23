"""Module to load the phrase dataset and match against target text. ===========

In this module:
  ChinesePhraseLoader: Extracts words from a chunk of text.
"""
import codecs


class ChinesePhraseLoader:
    """Loads the phrase dataset from the phrases.txt file.

    """

    FILE_NAME = '../data/dictionary/phrases.txt'

    def load():
        """Loads the phrases and returns a dict structure.

        """
        with codecs.open(FILE_NAME, 'r', "utf-8") as f:
            for line in f:
                pass

