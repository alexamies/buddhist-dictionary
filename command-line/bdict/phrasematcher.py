"""Module to load the phrase dataset and match against target text. ===========

In this module:
  ChinesePhraseLoader: Extracts words from a chunk of text.
"""
import codecs


class PhraseDataset:
    """Loads the phrase dataset from the phrases.txt file.

    """

    FILE_NAME = '../data/dictionary/phrases.txt'

    def Load(self):
        """Loads the phrases and returns a dictionary structure.

        The keys of the dictionary will be the traditional Chinese text for the phrases.
        The dictionary entries will contain the POS tagged text and other information.

        Returns:
          A dictionary structure with the phrase dataset.
        """
        self.phrases = {}
        with codecs.open(PhraseDataset.FILE_NAME, 'r', "utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                fields = line.split('\t')
                if fields and len(fields) >= 5:
                    entry = {}
                    entry['id'] = fields[0]
                    entry['chinese_phrase'] = fields[1]
                    entry['pos_tagged'] = fields[2]
                    entry['sanskrit'] = fields[3]
                    entry['source_no'] = fields[4]
                    entry['source_name'] = fields[5]
                    self.phrases[fields[1]] = entry
        return self.phrases

    def Matches(self, text):
        """Gets all the matches in the given text contains any phrases in the dataset.

        Scans all possible substrings of the text looking for matches against the
        phrase.

        Args:
          text: The text to search for matching phrases.

        Return:
          A list of entries for matching phrases, with an empty list for no matches.
        """
        matches = []
        for key in self.phrases.keys():
            if text.find(key) > -1:
                matches.append(self.phrases[key])
        return matches

