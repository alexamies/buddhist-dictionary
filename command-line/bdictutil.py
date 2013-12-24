"""Command line to compile a vocabulary from a text file. =====================

The words in the text file will be compared agains the Sanskrit dictionary.
"""
import locale
import sys

from bdict import chinesevocab
from bdict import corpusmanager
from bdict import glossgenerator
from bdict import sanskritvocab


def PrintUsage():
    print('Usage: python bdictutil.py <command> <arguments.')
    print('Supported commands: buildvocab, generategloss, listcorpus, help')
    print('The buildvocab command builds a vocabulary with word frequency '
          'analysis from a corpus document.')
    print('Usage: python bdictutil.py buildvocab <doc_num>')
    print('Example: python bdictutil.py buildvocab 1')
    print('Get the corpus document number from the listcorpus command.')
    print('The generategloss command generates a file with gloss in HTML format.')
    print('Usage: python bdictutil.py generategloss <doc_num>')
    print('The listcorpus command lists all the documents in the corpus (aka library).')
    print('Usage: python bdictutil.py listcorpus')


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
        corpus_entry = corpus[doc_num-1]
        language = corpus_entry['language']
        languages = ['Sanskrit', 'Chinese']
        if language not in languages:
            print('Language found %s is not supported' % language) 
            print('Please use one of these languages: %s' % languages) 
            sys.exit(2)
        if language == 'Sanskrit':
            vocab = sanskritvocab.SanskritVocabulary()
            vocab.BuildVocabulary(corpus_entry)
        elif language == 'Chinese':
            vocab = chinesevocab.ChineseVocabulary()
            vocab.BuildVocabulary(corpus_entry)
    elif command == 'generategloss':
        if len(sys.argv) < 3:
            print('A document number is required for the generategloss command')
            PrintUsage()
            sys.exit(2)
        doc_num = int(sys.argv[2])
        cmanager = corpusmanager.CorpusManager()
        corpus = cmanager.LoadCorpus()
        corpus_entry = corpus[doc_num-1]
        generator = glossgenerator.HTMLGlossGenerator()
        html = generator.WriteDoc(corpus_entry)
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

