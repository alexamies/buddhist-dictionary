"""Command line utility for illustration file management.

Copies files based on the entry in illustrations.txt.
"""
import sys


def main():


def CopyFiles(illustrations):
    """Copies files from the web site to the local system.

    Args:
      illustrations: an array of the illustrations
    """
    pass


def LoadIllustrations():
    """Loads the illustrations text file into an array.
    
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
            if len(tokens) > 10:
                entry['description'] = tokens[10]
            corpus.append(entry)
    return corpus


if __name__ == "__main__":
    main()

