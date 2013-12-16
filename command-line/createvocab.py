"""Command line to compile a vocabulary from a text file. =====================

The words in the text file will be compared agains the Sanskrit dictionary.
"""
import locale
import sys

from bdict import ChineseVocab
from bdict import SanskritVocab


def PrintUsage():
    print('Usage: python createvocab.py <command> <arguments.')
    print('Supported commands: buildvocab, listcorpus, help')
    print('The buildvocab command builds a vocabulary with word frequency '
          'analysis from a corpus document.')
    print('Usage: python createvocab.py buildvocab directory file language '
          '[outfile]')
    print('Example: python createvocab.py buildvocab ../web/corpus '
          'diamond-sutra-sanskrit1.txt sanskrit results.md')
    print('The listcorpus command lists all the documents in the corpus.')
    print('Usage: python createvocab.py listcorpus')


def main():
    locale.setlocale(locale.LC_ALL, '')
    if len(sys.argv) < 4:
        PrintUsage()
        sys.exit(2)
    command = sys.argv[1]
    if command == 'buildvocab':
        directory = sys.argv[2]
        infile = sys.argv[3]
        language = sys.argv[4]
        languages = ['sanskrit', 'chinese']
        outfile = sys.argv[5]
        if language not in languages:
            print('Please use one of these languages: %s' % languages) 
            sys.exit(2)
        if language == 'sanskrit':
            SanskritVocab.BuildVocabulary(directory, infile)
        elif language == 'chinese':
            ChineseVocab.BuildVocabulary(directory, infile, outfile)
    elif command == 'listcorpus':
        print('The listcorpus command lists all the documents in the corpus.')
    elif command == 'help':
        PrintUsage()
    else:
        print('Do not understand command.')
        PrintUsage()

if __name__ == "__main__":
    main()

