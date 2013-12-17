"""Command line to compile a vocabulary from a text file. =====================

The words in the text file will be compared agains the Sanskrit dictionary.
"""
import locale
import sys

from bdict import configmanager
from bdict import corpusmanager
from bdict import chinesevocab
from bdict import sanskritvocab


def PrintUsage():
    print('Usage: python createvocab.py <command> <arguments.')
    print('Supported commands: buildvocab, listcorpus, help')
    print('The buildvocab command builds a vocabulary with word frequency '
          'analysis from a corpus document.')
    print('Usage: python createvocab.py buildvocab <doc_num>')
    print('Example: python createvocab.py buildvocab 0')
    print('Get the corpus document number from the listcorpus command.')
    print('The listcorpus command lists all the documents in the corpus (aka library).')
    print('Usage: python createvocab.py listcorpus')


def main():
    locale.setlocale(locale.LC_ALL, '')
    if len(sys.argv) < 2:
        PrintUsage()
        sys.exit(2)
    command = sys.argv[1]
    if command == 'buildvocab':
        if len(sys.argv) < 3:
            print('A document number is required for the buildvocab command')
            PrintUsage()
            sys.exit(2)
        doc_num = int(sys.argv[2])
        cmanager = corpusmanager.CorpusManager()
        corpus = cmanager.LoadCorpus()
        corpus_entry = corpus[doc_num]
        infile = corpus_entry['plain_text']
        language = corpus_entry['language']
        languages = ['Sanskrit', 'Chinese']
        if language not in languages:
            print('Language found %s is not supported' % language) 
            print('Please use one of these languages: %s' % languages) 
            sys.exit(2)
        manager = configmanager.ConfigurationManager()
        config = manager.LoadConfig()
        corpus_directory = config['corpus_directory']
        if language == 'Sanskrit':
            sanskritvocab.BuildVocabulary(corpus_directory, infile)
        elif language == 'Chinese':
            vocab = chinesevocab.ChineseVocabulary()
            vocab.BuildVocabulary(corpus_directory, infile)
    elif command == 'listcorpus':
        cmanager = corpusmanager.CorpusManager()
        cmanager.PrintCorpus()
    elif command == 'help':
        PrintUsage()
    else:
        print('Did not understand command.')
        PrintUsage()

if __name__ == "__main__":
    main()

