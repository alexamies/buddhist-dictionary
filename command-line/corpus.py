"""Module to read the corpus metadata.

The corpus documents are listed in the file /data/corpos/corpus.txt
"""

from jinja2 import Environment, FileSystemLoader, Template


def main():
    """Command line entry point.
    
    Use this if you want to drive this module from the command line directly.
    """
    corpus = LoadCorpusMeta()
    PrintCorpusMeta(corpus)


def LoadCorpusMeta():
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
                entry['uri'] = tokens[5]
            if len(tokens) > 6:
                entry['source'] = tokens[6]
            if len(tokens) > 7:
                entry['start'] = tokens[7]
            if len(tokens) > 8:
                entry['end'] = tokens[8]
            if len(tokens) > 9:
                entry['description'] = tokens[9]
            corpus.append(entry)
    return corpus


def PrintCorpusMeta(corpus):
    """Loads the corpus text file into memory.
    
    Args:
        corpus: a list of corpus entries
    """
    dirname = 'templates'
    output_dir = '../web/'
    filename = 'corpus.html'
    output_file = '%s%s' % (output_dir, filename)
    loader = FileSystemLoader(dirname)
    env = Environment(loader=loader)
    template = env.get_template(filename)
    template.stream(corpus=corpus).dump(output_file)


if __name__ == "__main__":
    main()

