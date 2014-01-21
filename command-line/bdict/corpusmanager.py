"""Module to read the corpus (aka library) data. ==============================

The corpus documents are listed in the file $PROJECT_HOME/data/corpos/corpus.txt
"""
import codecs

CORPUS_FILE = 'corpus.txt'
JSON_FILE = 'corpus.json'
JSON_DIR = '../web/script/'

class CorpusManager:
    """Reads and prints the corpus data.

    Loads the corpus based on entries in corpus file.
    """

    def GetAllTagged(self):
        """Returns a list of corpus entries for all POS tagged documents in the corpus.

        Returns:
            A list of corpus entries.
        """
        tagged_entries = []
        corpus = self.LoadCorpus()
        for entry in corpus:
            if 'pos_tagged' in entry:
                tagged_entries.append(entry)
        return tagged_entries

    def LoadCorpus(self):
        """Loads the corpus text file into memory.

        Returns:
            A list of corpus entries.
        """
        dirname = '../data/dictionary/'
        fullpath = '%s%s' % (dirname, CORPUS_FILE)
        corpus = []
        with codecs.open(fullpath, 'r', "utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
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
                        if tokens[9].strip() != u'\\N':
                        	entry['end'] = tokens[9]
                    if len(tokens) > 10:
                        if tokens[10].strip() != u'\\N':
                        	entry['plain_text'] = tokens[10].strip()
                    if len(tokens) > 11:
                        if tokens[11].strip() != u'\\N':
                        	entry['translator'] = tokens[11].strip()
                    if len(tokens) > 12:
                        if tokens[12].strip() != u'\\N':
                        	entry['reference'] = tokens[12].strip()
                    if len(tokens) > 13:
                        if tokens[13].strip() != u'\\N':
                        	entry['genre'] = tokens[13].strip()
                    if len(tokens) > 14:
                        if tokens[14].strip() != u'\\N':
                        	entry['period'] = tokens[14].strip()
                    if len(tokens) > 15:
                        if tokens[15].strip() != u'\\N':
                        	entry['pos_tagged'] = tokens[15].strip()
                    if len(tokens) > 16:
                        if tokens[16].strip() != u'\\N':
                        	entry['analysis_file'] = tokens[16].strip()
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

    def GenCorpusJSON(self):
        """Prints the corpus data out in json format.
 
        Loads the corpus from the corpus.txt file and translates into JSON.

        Returns:
          The name of the file written to.
        """
        corpus = self.LoadCorpus()
        output_file = '%s%s' % (JSON_DIR, JSON_FILE)
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
        return output_file
