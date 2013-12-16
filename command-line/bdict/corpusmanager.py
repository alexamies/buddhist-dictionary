"""Module to read the corpus (aka library) data. ==============================

The corpus documents are listed in the file $PROJECT_HOMEA/data/corpos/corpus.txt
"""


class CorpusManager:
    """Reads and prints the corpus data.

        Not finished yet.
    """

def LoadCorpus():
    """Loads the corpus text file into memory.
    
    Returns:
        A list of corpus entries.
    """
    dirname = '../data/corpus/'
    filename = 'corpus.txt'
    fullpath = '%s%s' % (dirname, filename)
    f = open(fullpath, 'r')
    corpus = []
    for line in f:
        tokens = line.split('\t')
        if tokens:
            entry = {}
            entry['id'] = tokens[0]
            if len(tokens) > 1:
                entry['source_name'] = tokens[1]
            if len(tokens) > 2:
                entry['type'] = tokens[2]
            if len(tokens) > 3:
                entry['language'] = tokens[3]
            if len(tokens) > 4:
                entry['charset'] = tokens[4]
            if len(tokens) > 5:
                entry['doc_type'] = tokens[5]
            if len(tokens) > 6:
                entry['uri'] = tokens[6]
            if len(tokens) > 7:
                entry['source'] = tokens[7]
            if len(tokens) > 8:
                entry['start'] = tokens[8]
            if len(tokens) > 9:
                entry['end'] = tokens[9]
            corpus.append(entry)
    return corpus


def PrinCorpus(corpus):
    """Prints the corpus data to standard output.
    
    Args:
        corpus: a list of corpus entries
    """

