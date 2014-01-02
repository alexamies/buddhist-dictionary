"""Command line to compile a vocabulary from a text file. =====================

The words in the text file will be compared agains the Sanskrit dictionary.
"""
import locale
import sys

from bdict import app_exceptions
from bdict import chinesevocab
from bdict import configmanager
from bdict import corpusmanager
from bdict import glossgenerator
from bdict import postaggeraccuracy
from bdict import sanskritvocab
from bdict import taggeddoc


def PrintUsage():
    print(
"""Usage: python bdictutil.py <command> <arguments.
Supported commands: buildvocab, generategloss, help, listcorpus, tag wordsensefreq.

The buildvocab command builds a vocabulary with word frequency analysis from a
corpus document. Usage:

    python bdictutil.py buildvocab <doc_num>

Example:

    python bdictutil.py buildvocab 1

Get the corpus document number from the listcorpus command.

The generategloss command generates a file with gloss in HTML format. Usage:

    python bdictutil.py generategloss <doc_num>

The listcorpus command lists all the documents in the corpus (aka library).
Usage:

    python bdictutil.py listcorpus

The tag command generates part-of-speech tags for a document in the corpus.
Usage:

    python bdictutil.py tag <doc_num>


The wordsensefreq command generates word sense frequency from part-of-speech
tagged documents in the corpus. Usage:

    python bdictutil.py wordsensefreq <doc_num>
""")

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
            outfile = vocab.BuildVocabulary(corpus_entry)
            print('Wrote output file %s ' % outfile)
    elif command == 'generategloss':
        if len(sys.argv) < 3:
            print('A document number is required for the generategloss command')
            PrintUsage()
            sys.exit(2)
        doc_num = int(sys.argv[2])
        cmanager = corpusmanager.CorpusManager()
        corpus = cmanager.LoadCorpus()
        corpus_entry = corpus[doc_num-1]
        generator = glossgenerator.GlossGenerator()
        filename = generator.WriteDoc(corpus_entry)
        print('Wrote output to file %s' % filename)
    elif command == 'help':
        PrintUsage()
    elif command == 'listcorpus':
        cmanager = corpusmanager.CorpusManager()
        cmanager.PrintCorpus()
    elif command == 'tag':
        if len(sys.argv) < 3:
            print('A document number is required for the tag command')
            PrintUsage()
            sys.exit(2)
        doc_num = int(sys.argv[2])
        cmanager = corpusmanager.CorpusManager()
        corpus = cmanager.LoadCorpus()
        corpus_entry = corpus[doc_num-1]
        generator = glossgenerator.GlossGenerator(output_type=glossgenerator.POS_TAGGED_TYPE)
        filename = generator.WriteDoc(corpus_entry)
        print('Wrote output to file %s' % filename)
        if 'pos_tagged' in corpus_entry:
            try:
                pos_tagged = corpus_entry['pos_tagged']
                manager = configmanager.ConfigurationManager()
                config = manager.LoadConfig()
                tagged_directory = config['tagged_directory']
                standard_file = '%s/%s' % (tagged_directory, pos_tagged)
                standard = taggeddoc.LoadTaggedDoc(standard_file)
                subject = taggeddoc.LoadTaggedDoc(filename)
                accuracy = postaggeraccuracy.TaggerAccuracy(standard, subject)
                print('Tagging accuracy: %f' % accuracy)
            except app_exceptions.BDictException as e:
                print('Could not compute accuracy: %s.' % e)
        else:
            print('Could not compute accuracy: no standard tagged file.')
    elif command == 'wordsensefreq':
        outfile = 'unigram_freq.txt'
        if len(sys.argv) < 3:
            print('Word sense frequency will be computed for all corpus entries '
                  'with a tagged document.')
            wfreq = taggeddoc.WordSenseForCorpus()
            taggeddoc.SaveWordSenseFreq(wfreq, outfile)
        else:
            doc_num = int(sys.argv[2])
            cmanager = corpusmanager.CorpusManager()
            corpus = cmanager.LoadCorpus()
            corpus_entry = corpus[doc_num-1]
            try:
                wfreq = taggeddoc.WordSenseFrequency(corpus_entry)
                taggeddoc.SaveWordSenseFreq(wfreq, outfile)
            except app_exceptions.BDictException as e:
                print(e)
    else:
        print('Did not understand command.')
        PrintUsage()

if __name__ == "__main__":
    main()

