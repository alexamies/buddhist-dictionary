"""Module to read the corpus metadata.

The corpus documents are listed in the file /data/corpos/corpus.txt
"""
import codecs
import json

from bdict import corpusmanager


def main():
    """Command line entry point.
    
    Use this if you want to drive this module from the command line directly.
    """
    cmanager = corpusmanager.CorpusManager()
    corpus = cmanager.LoadCorpus()
    PrintCorpusMeta(corpus)


def PrintCorpusMeta(corpus):
    """Prints the corpus data out in json format.
 
    Args:
        corpus: a list of corpus entries
    """
    output_dir = ''
    filename = 'corpus.json'
    output_file = '%s%s' % (output_dir, filename)
    print('Writing %d entries to file %s' % (len(corpus), output_file))
    print(json.dumps({'corpus': ['a list']}))
    with codecs.open(output_file, 'w') as f:
        f.write(json.dumps({'corpus': corpus}))
        f.close()


if __name__ == "__main__":
    main()

