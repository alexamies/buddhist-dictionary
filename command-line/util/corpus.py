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
    with codecs.open(output_file, 'w', "utf-8") as f:
        f.write('[')
        for i in range(len(corpus)):
            doc = corpus[i]
            f.write('{')
            j = 0
            for key in doc.keys():
                if doc[key] == '\\N':
                    f.write('"%s": ""' % (key))
                else:
                    f.write('"%s": "%s"' % (key, doc[key]))
                if j != len(doc.keys()) - 1:
                    f.write(',')
                j += 1
            f.write('}\n')
            if i != len(corpus) - 1:
                f.write(',\n')
        f.write(']')
        f.close()


if __name__ == "__main__":
    main()

