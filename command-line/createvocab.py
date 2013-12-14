"""Command line to compile a vocabulary from a text file. =====================

The words in the text file will be compared agains the Sanskrit dictionary.
"""
import locale
import sys

from bdict import SanskritVocab


def main():
    locale.setlocale(locale.LC_ALL, '')
    if len(sys.argv) < 3:
        print('Usage: python createvocab.py directory file')
        print('Example: python createvocab ../web/corpus diamond-sutra-sanskrit1.txt')
        sys.exit(2)
    else:
        directory = sys.argv[1]
        infile = sys.argv[2]
        SanskritVocab.BuildVocabulary(directory, infile)


if __name__ == "__main__":
    main()

