"""Command line to compile a vocabulary from a text file. =====================

The words in the text file will be compared agains the Sanskrit dictionary.
"""
import locale
import sys

from bdict import ChineseVocab
from bdict import SanskritVocab


def main():
    locale.setlocale(locale.LC_ALL, '')
    if len(sys.argv) < 4:
        print('Usage: python createvocab.py directory file language [outfile]')
        print('Example: python createvocab.py ../web/corpus diamond-sutra-sanskrit1.txt sanskrit results.md')
        sys.exit(2)
    directory = sys.argv[1]
    infile = sys.argv[2]
    language = sys.argv[3]
    languages = ['sanskrit', 'chinese']
    outfile = sys.argv[4]
    if language not in languages:
        print('Please use one of these languages: %s' % languages) 
        sys.exit(2)
    if language == 'sanskrit':
        SanskritVocab.BuildVocabulary(directory, infile)
    elif language == 'chinese':
        ChineseVocab.BuildVocabulary(directory, infile, outfile)


if __name__ == "__main__":
    main()

