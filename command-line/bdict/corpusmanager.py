"""Module to read the corpus (aka library) data. ==============================

The corpus documents are listed in the file $PROJECT_HOMEA/data/corpos/corpus.txt
"""
import codecs


class CorpusManager:
    """Reads and prints the corpus data.

    """

    def LoadCorpus(self):
        """Loads the corpus text file into memory.

        Returns:
            A list of corpus entries.
        """
        dirname = '../data/dictionary/'
        filename = 'corpus.txt'
        fullpath = '%s%s' % (dirname, filename)
        corpus = []
        with codecs.open(fullpath, 'r', "utf-8") as f:
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
                        entry['plain_text'] = tokens[10].strip()
                    if len(tokens) > 11:
                        entry['translator'] = tokens[11].strip()
                    if len(tokens) > 12:
                        entry['reference'] = tokens[12].strip()
                    if len(tokens) > 13:
                        entry['genre'] = tokens[13].strip()
                    corpus.append(entry)
        return corpus

    def PrintCorpus(self):
        """Prints the corpus data to standard output.

        Only the entries with plain text files are printed because those are
        only files that the command line tool can operate on.

        Args:
            corpus: a list of corpus entries
        """
        corpus = self.LoadCorpus()
        print('Corpus entries with plain text files')
        for entry in corpus:
            if 'plain_text' in entry:
                print('%s\t%s\t%s' % (entry['id'], entry['source_name'], entry['plain_text']))

