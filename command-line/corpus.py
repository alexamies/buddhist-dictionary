"""Module to read the corpus metadata.

The corpus documents are listed in the file /data/corpos/corpus.txt
"""


def main():
    LoadCorpusMeta()


def LoadCorpusMeta():
    dirname = '../data/corpus/'
    filename = 'corpus.txt'
    fullpath = '%s%s' % (dirname, filename)
    f = open(fullpath, 'r')
    for line in f:
        words = line.split()
        if words:
            print(words[0])


if __name__ == "__main__":
    main()

