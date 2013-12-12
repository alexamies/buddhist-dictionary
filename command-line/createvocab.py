"""Command line to compile a vocabulary from a text file. =====================

The words in the text file will be compared agains the Sanskrit dictionary.
"""
import sys

from bdict import SanskritVocab


def BuildVocabulary(infile, sdict):
    """Builds the list of known and unknown words from the input file.
    """
    f = open(infile, 'r')
    wc = 0
    known_words = set()
    new_words = set()
    for line in f:
        if line.find('---END---') != -1:
            break
        words = line.split()
        wc += len(words)
        for word in words:
            if word in sdict:
                known_words.add(word)
            else:
                new_words.add(word)
    print('Word count: %d, known words: %d, new words: %d' % 
          (wc, len(known_words), len(new_words)))
    print('Known words:')
    PrintVocab(known_words)
    print()
    print('New words')
    return new_words


def OpenDictionary(fullpath):
    """Reads the dictionary into memory
    """
    f = open(fullpath, 'r')
    sdict = {}
    for line in f:
        line = line.strip()
        if not line:
            continue
        fields = line.split('\t')
        if fields and len(fields) >= 10:
            sid = fields[0]
            cid = fields[1]
            slatin = fields[2]
            iast = fields[3]
            sdict[iast] = fields
    return sdict


def main():
    if len(sys.argv) < 2:
        print('Please supply the name of a file.')
        sys.exit(2)
    else:
        infile = sys.argv[1]
        print('Compiling vocabulary from file: %s' % (infile))
        ddirname = '../data/dictionary/'
        dfilename = 'sanskrit.txt'
        fullpath = '%s%s' % (ddirname, dfilename)
        sdict = OpenDictionary(fullpath)
        new_words = BuildVocabulary(infile, sdict)
        SanskritVocab.PrintVocab(new_words)


if __name__ == "__main__":
    main()

